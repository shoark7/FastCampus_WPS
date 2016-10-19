from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


