from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display=("last_name","first_name","email","username")

admin.site.register(CustomUser,CustomUserAdmin)