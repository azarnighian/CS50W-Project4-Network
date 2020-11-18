from django.contrib.auth.models import AbstractUser
from django.db import models

class Posts(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    creation_datetime = models.DateTimeField() 
    likes = models.IntegerField(default=0)
    
class User(AbstractUser):
    followers = models.ManyToManyField('self', related_name="following", symmetrical=False)
    liked_posts = models.ManyToManyField(Posts, blank=True, related_name="likers")

                    
                    
                    # After every change:
                    # python3 manage.py makemigrations
                    # python3 manage.py migrate