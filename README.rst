==============
django-jsonify
==============

Abstract
--------
jsonify filter for Django based on http://djangosnippets.org/snippets/201/

Installation
------------
To install simply use:
pip install django-jsonify

Usage
-----
Django template:

    {% load jsonify %}
    
    {% block content %} <script type="text/javascript">
        <![CDATA[ var items = {{ items|jsonify }}; ]]></script>
    {% endblock %}
