from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class YoutubeManager(UserManager):
    pass
# 얘네 받으면 그냥 하는 것이랑 똑같다.

class YoutubeUser(AbstractUser):


    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자들'


