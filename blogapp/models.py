from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone
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
    
class Blog(models.Model):
    CATEGORY = (
    ("tech", "Texnologiya"),
    ("econ", "Iqtisodiyot"),
    ("biz", "Biznes"),
    )
    title=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255,blank=True,unique=True)
    content=models.TextField()
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='blogs',null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    published_time=models.DateTimeField(blank=True,null=True)
    is_draft=models.BooleanField(default=True)
    category=models.CharField(choices=CATEGORY,blank=True,null=True,max_length=255)
    featured_image=models.ImageField(upload_to='blog_images',blank=True,null=True)

    class Meta:
        ordering=['-created_at']

    def __str__(self) -> str:
        return self.title

    def save(self,*args,**kwargs):
        base_slug=slugify(self.title,allow_unicode=True) 
        slug=base_slug
        num=1
        while Blog.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug=f'{base_slug}-{num}'
            num+=1
        self.slug=slug       

        if not self.is_draft and self.published_time  is None:
            self.published_time=timezone.now()

        super().save(*args,**kwargs)    
 