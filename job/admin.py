from django.contrib import admin
from .models import JobPost,JobCategory

# Register your models here.
admin.site.register(JobPost)
admin.site.register(JobCategory)
