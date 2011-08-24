from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.utils import simplejson
from django.template import Library

register = Library()

def jsonify(object):
    if isinstance(obj, QuerySet):
        return serialize('json', obj)
    return simplejson.dumps(obj)

register.filter('jsonify', jsonify)
