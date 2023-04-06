from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(blank=True, null=True, max_length=200)
    text = models.CharField(max_length=500)
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)
    objects = models.Manager
    DoesNotExist = models.Manager

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
