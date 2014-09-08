from django.template import Template, Context
from django.test import TestCase

class JsonifyTemplateTagsTestCase(TestCase):
    def setUp(self):
        pass

    def test_jsonify_object(self):
        template = Template("{% load jsonify %}{{ the_object|jsonify }}")
        the_object = {u"key": u"value"}
        context = Context({
            'the_object': the_object
        })
        self.assertEqual(template.render(context), u'{"key": "value"}')

