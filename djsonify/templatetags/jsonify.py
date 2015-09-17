import django
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.query import QuerySet
from django.utils.safestring import mark_safe
from django.template import Library

# This part is REALLY important to make it work properly, specially on the transition between Django 1.4 and 1.5.
# If we want to avoid any backward compatibility issue, specially if you have installed simplejson, you should be sure that
# the json library you are using is the same as DjangoJSONEncoder one.
if django.VERSION < (1, 5):
    from django.utils import simplejson as json
    # This module has been deprecated in 1.5, and DjangoJSONEncoder is inheriting from json.JSONEncoder from 1.5+
    # (was inheriting from simplejson.JSONEncoder before)
    # So we should ensure that the json module we are importing for dumps/loads/... is the same as DjangoJSONEncoder one.
else:
    import json


register = Library()

@register.filter
def jsonify(obj):
    if isinstance(obj, QuerySet):
        return mark_safe(serialize('json', obj))
    return mark_safe(json.dumps(obj, cls=DjangoJSONEncoder))
