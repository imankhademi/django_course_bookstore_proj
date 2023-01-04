from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
