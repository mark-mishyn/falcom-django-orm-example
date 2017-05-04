import binascii
import os

from django.db import models
from model_utils.models import TimeStampedModel


class ExampleUser(models.Model):
    """
    Just example model to built example controllers
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class AuthToken(TimeStampedModel):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(ExampleUser, related_name='auth_token', on_delete=models.CASCADE)

    def __str__(self):
        return self.key

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = binascii.hexlify(os.urandom(20)).decode()
        return super().save(*args, **kwargs)
