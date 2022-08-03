from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    link = models.URLField(max_length=1000)
    shortlink = models.URLField(max_length=1000)


    def __str__(self):
        return self.author
