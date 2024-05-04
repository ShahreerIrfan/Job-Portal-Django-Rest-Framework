from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'', views.UserProfileViewSet)
router.register(r'todo', views.TodoViewset, basename='todo')  # Remove the trailing slash here

urlpatterns = [
    path('', include(router.urls)),
]