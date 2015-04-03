Boring Flask App!
=================

.. image:: https://circleci.com/gh/troxor/flaskapp.png?circle-token=:circle-token
       :target: https://circleci.com/gh/troxor/flaskapp

Requirements
------------

- Python 2 or 3
- Modules in requirements.txt
- Low expectations for a web application


Getting Started
===============

Docker Quickstart
-----------------

::
    $ pip install fig
    $ fig build
    $ fig up

Configuration
-------------

Application is configured via environment variables. Priority:

1. (honcho) .env file
2. cmdline environment vars
3. (fig) fig.yml
4. Hardcoded bare minimum vars in config.py

::

    $ cp .env.example .env ; vim .env
    $ pip install -r requirements.txt


Running
-------
::
    $ honcho start web

or 

::
    $ python -m flaskapp

::

    Deploy under a WSGI server
    $ python -m flaskapp.wsgi

