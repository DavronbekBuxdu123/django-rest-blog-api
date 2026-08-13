from django.urls import path
from .views import user_register,create_blog
urlpatterns=[
    path("user_register/",user_register,name='user_register'),
    path("create_blog/",create_blog,name='create_blog'),
]