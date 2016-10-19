from django.db import models

# Create your models here.
class Star(models.Model):
    title = models.CharField(max_length=50)
    video_id = models.CharField(max_length=20, unique=True)
    published_date = models.DateField()
    image_url = models.URLField(max_length=50)

    class Meta:
        ordering = ['-published_date', 'title']