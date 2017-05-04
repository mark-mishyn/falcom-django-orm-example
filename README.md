# Falcon + Django ORM Example

Example of Python REST API built with Falcon and Django ORM

### Core technologies:
* Falcon 1.1
* Django 1.11 (for ORM and admin panel)


### Development
This web application was built for Python 3 only.

To run application for development use following command:

`gunicorn --reload  --timeout 999 app:api`

*Note: DJANGO_SETTINGS_MODULE environment variable must be set* 
