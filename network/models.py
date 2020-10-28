from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Posts(models.Model):
    username = models.CharField(max_length=20)
    content = models.TextField()
    creation_datetime = models.DateTimeField() 
    likes = models.IntegerField(default=0)