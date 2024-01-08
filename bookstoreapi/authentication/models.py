# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_no = models.CharField(max_length=20)
    bio = models.CharField(max_length=50)
    profile_photo = models.ImageField(upload_to='images/',null=True)
    def __str__(self):
        return self.username
