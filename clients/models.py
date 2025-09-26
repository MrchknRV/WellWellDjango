from django.db import models
from django.contrib.auth.models import AbstractUser


class Client(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to="client/avatar", blank=True, null=True)
    phone_number = models.CharField(max_length=17, blank=True, null=True)
    country = models.CharField(max_length=56, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
