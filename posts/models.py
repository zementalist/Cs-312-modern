from django.db import models
from django.utils.text import Truncator


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    likes = models.IntegerField(default=0)

    kids_allowed = models.BooleanField(default=True)


    