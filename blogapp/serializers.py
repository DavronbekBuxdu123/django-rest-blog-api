from rest_framework import serializers
from django.contrib.auth import get_user_model

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