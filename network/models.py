from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # followers = 
    # following = 
    pass

class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation_datetime = models.DateTimeField() 
    likes = models.IntegerField(default=0)


                    # After every change:
                    # python3 manage.py makemigrations
                    # python3 manage.py migrate