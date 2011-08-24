jsonify filter for Django based on http://djangosnippets.org/snippets/201/

To install simply use:
pip install django-jsonify

Then in templates:

{% load jsonify %}

{% block content %} <script type="text/javascript">
    <![CDATA[ var items = {{ items|jsonify }}; ]]></script>
{% endblock %}
