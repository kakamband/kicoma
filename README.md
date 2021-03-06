KiCoMa - Kitchen cooking management
==================

[![GitHub release](https://img.shields.io/github/release-pre/valasek/kicoma.svg)](https://github.com/valasek/kicoma)
[![GitHub issues](https://img.shields.io/github/issues/valasek/kicoma.svg)](https://github.com/valasek/kicoma/issues)
[![Build Status](https://travis-ci.org/valasek/kicoma.svg?branch=master)](https://travis-ci.org/valasek/kima) [![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/) [![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Demo
Check the lastest version at [kicoma.herokuapp.com](https://kicoma.herokuapp.com).

## License

All source code in the [KiCoMa](https://github.com/valasek/kima) is available under the GNU GPL v3 License. See [LICENSE.md](LICENSE.md) for details.

## Data Model

![Data model](./kicoma/static/images/datamodel.png)

# Useful Commands

## Reset Development DB
`./reset-db.sh`

## Reset Heroku DB
`./reset-db-heroku.sh`

## Check the production settings
./manage.py check --deploy --settings=config.settings.production

## Generate DB model
Using https://django-extensions.readthedocs.io/en/latest/graph_models.html
* `python3 manage.py graph_models -a -g -o datamodel.png` or
* `python3 manage.py graph_models kitchen -g -o datamodel.png` and copy the file to statics/images

## Update Translations
### Generate message files for a desired language
`./manage.py makemessages -l cs_CZ --ignore=env/*`
 
### After adding translations to the .po files, compile the messages
`./manage.py compilemessages`

# Deploy to Heroku

## Initial set-up
https://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html

## Set email domain
`heroku config:set MAILGUN_DOMAIN=hospic-cercany.cz`

## Update
`git push heroku master`

## Generate user password for fixture

`./manage.py shell`
`from django.contrib.auth.hashers import make_password`
`make_password('password')`


## External dependencies

* Python
* Django
* Postgresql
* wkhtmltopdf**

Local
- `sudo apt-get install wkhtmltopdf`

Heroku
- https://github.com/tutorcruncher/pydf
- https://github.com/dscout/wkhtmltopdf-buildpack
- https://razorjack.net/wkhtmltopdf-on-heroku-evaluating-different-installation-options/


## Getting started

To get started with the app, clone the repo and then install Python 3 and Django 3.0:

```
$ cd ~/tmp
$ git clone https://github.com/valasek/kima
$ cd kima
```

Next, migrate the database:

```
$ ./manage.py makemigrations
$ ./manage.py migrate
```

Finally, run the test suite to verify that everything is working correctly:

```
$ ./manage.py test
```

If the test suite passes, you'll be ready to run the app in a local server:

```
$ ./manage.py runserver
```


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy kicoma

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html




Getting up and running locally:
https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html
