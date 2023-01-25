from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    photo = CloudinaryField("image", blank=True, null=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []
