from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    #followers = models.ManyToManyField('User', blank=True)
    def __str__(self):
        return f"{self.username}"


