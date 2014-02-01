from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.CharField(max_length=255, null=False, blank=False, unique=True)
    author = models.ForeignKey(User, related_name='posts')
    content = models.TextField(blank=True, default='')
    publish_time = models.DateTimeField(default=datetime.now)