from django.db import models
from django.contrib.auth.models import User as BaseUser


class User(BaseUser):
    age = models.IntegerField(null=True, blank=True)

    occupation = models.CharField(
        max_length=100,
        blank=True
    )