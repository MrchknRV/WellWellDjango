from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=35, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=17, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatar/", blank=True, null=True)
    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username