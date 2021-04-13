# Falcon + Django ORM Example

**Example of REST API built with Falcon and Django ORM**



### Overview
Code provides example how to use Django ORM + Falcon for rapid REST API development. 

*Note: application supports Python 3 only.*

### Generic classes
#### middlewares
* JSONResponseMiddleware
* TokenAuthenticationMiddleware

#### controllers and mixins for CRUD operations
* ListModelResource
* SingleModelResource
* ListMixin
* CreateMixin
* RetrieveMixin
* DestroyMixin
* UpdateMixin

#### pagination
* LimitOffsetPaginator


### Core technologies:
* Falcon 3
* Django 3.2 (for ORM and (optional) admin panel)
* marshmallow 3


### Development
To run application for development use the following command:

`gunicorn --reload  --timeout 999 app:api`

*Note: DJANGO_SETTINGS_MODULE environment variable must be set. You can start with simple `export DJANGO_SETTINGS_MODULE="settings"`*
