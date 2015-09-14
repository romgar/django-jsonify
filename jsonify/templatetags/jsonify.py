import django
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.query import QuerySet
from django.utils.safestring import mark_safe
from django.template import Library

# This part is REALLY important to make it work properly, specially on the transition between Django 1.4 and 1.5.
# From 1.5, Django is internally using standard json library, and it means that :
# - DjangoJSONEncoder was inheriting from simplejson.JSONEncoder, and that simplejson was imported from django.utils
# - DjangoJSONEncoder now inherits from json.JSONEncoder, which is the standard json library.
# If we want to avoid any backward compatibility issue, we need to take care of these different imports while using
# internal DjangoJSONEncoder.
if django.VERSION < (1, 5):
    # This module has been deprecated in 1.5
    from django.utils import simplejson as json
else:
    import json


register = Library()

@register.filter
def jsonify(obj):
    if isinstance(obj, QuerySet):
        return mark_safe(serialize('json', obj))
    return mark_safe(json.dumps(obj, cls=DjangoJSONEncoder))
