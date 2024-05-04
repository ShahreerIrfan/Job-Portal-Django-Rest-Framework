from django.contrib import admin
from .models import UserProfile,Todo

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Todo)
