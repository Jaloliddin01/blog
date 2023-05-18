from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    post_text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
