from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class JobCategory(models.Model):
    category = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.category

class JobPost(models.Model):
    poster = models.ForeignKey(User,on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    job_category = models.ForeignKey(JobCategory,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.job_title
    