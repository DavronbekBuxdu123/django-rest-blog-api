from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    bio=models.TextField(blank=True,null=True)
    profile_picture=models.ImageField(blank=True,null=True,upload_to='profile_img')
    instagram=models.CharField(max_length=255,blank=True,null=True)
    youtube=models.CharField(max_length=255,blank=True,null=True)
    twitter=models.CharField(max_length=255,blank=True,null=True)
    facebook=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self) -> str:
        return self.username