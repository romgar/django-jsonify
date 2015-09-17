import pytest

from django.template import Template, Context

def test_jsonify_object():
    template = Template("{% load jsonify %}{{ the_object|jsonify }}")
    the_object = {u"key": u"value"}
    context = Context({
        'the_object': the_object
    })
    assert template.render(context) == u'{"key": "value"}'
