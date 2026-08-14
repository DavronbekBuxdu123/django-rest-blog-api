from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Blog

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=['id','last_name','first_name','username','email','password']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def create(self,validated_data):
        username=validated_data["username"]
        first_name=validated_data['first_name']
        last_name=validated_data['last_name'] 
        email=validated_data['email']
        password=validated_data['password']

        user=get_user_model()
        new_user=user.objects.create(username=username,first_name=first_name,last_name=last_name,email=email)   
        new_user.set_password(password)
        new_user.save()
        return new_user
    

class SimpleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "first_name", "last_name"]

class BlogSerializer(serializers.ModelSerializer):
    author = SimpleAuthorSerializer(read_only=True)
    class Meta:
        model=Blog 
        fields=['id','title','slug','author','category','content','featured_image','published_time','is_draft','created_at','updated_at']