from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    introduction = models.CharField(blank=True, max_length=255)
    profile_photo = models.ImageField()
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')