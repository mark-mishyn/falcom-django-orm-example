# Falcon + Django ORM Example

**Example of a REST API that was built with Falcon and Django ORM**

This repo provides an example of how to use Django ORM + Falcon for rapid REST API development. You can check very basic example of usage in **controller.py**

#### Core technologies:
* Falcon 3
* Django 3.2 (for ORM and (optional) admin panel)
* marshmallow 3

There are batch of handy generic classes in the repo. These classes can be used to quickly build APIs.

#### 1. CRUD controllers 
* ListModelResource
* SingleModelResource

#### 2. CRUD controllers mixins 
* ListMixin
* CreateMixin
* RetrieveMixin
* DestroyMixin
* UpdateMixin

#### 3. middlewares
* JSONResponseMiddleware
* TokenAuthenticationMiddleware

#### 4. pagination
* LimitOffsetPaginator

### Development
To run application for development use the following command:
`gunicorn --reload  --timeout 999 app:api`

*Note: DJANGO_SETTINGS_MODULE environment variable must be set. You can start with simple `export DJANGO_SETTINGS_MODULE="settings"`*
