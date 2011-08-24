==============
django-jsonify
==============

Abstract
--------
JSON library for working with django + json

Donors
------
jsonify filter for Django based on http://djangosnippets.org/snippets/201/
and JSONResponse + ajax_request decorator from django-annoying https://bitbucket.org/offline/django-annoying (Anderson <self.anderson@gmail.com>)

Installation
------------
To install simply use:
pip install django-jsonify

Usage
-----
Django template:


::

    {% load jsonify %}
    
    {% block content %} <script type="text/javascript">
        <![CDATA[ var items = {{ items|jsonify }}; ]]></script>
    {% endblock %}
