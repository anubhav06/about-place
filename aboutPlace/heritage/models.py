from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    def __str__(self):
        return f"{self.username}"


# Add image field and likes field later if time left
class Posts(models.Model):

    content =  models.CharField(max_length=2000, default=None)
    country = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poster")
    

    def __str__(self):
        return f"{self.poster} : {self.content}"