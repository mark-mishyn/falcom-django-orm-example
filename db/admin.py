from django.contrib import admin
from django.contrib.auth.models import Group

from db.models import AuthToken, ExampleUser

admin.site.unregister(Group)


@admin.register(AuthToken)
class AuthTokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created')


@admin.register(ExampleUser)
class AuthTokenAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_of_birth')

