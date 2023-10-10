from django.db import models

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    comments = models.TextField()
    link = models.URLField()
