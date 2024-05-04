from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to="User/images/profile_photo",null=True)
    def __str__(self) -> str:
        return self.user.first_name

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title