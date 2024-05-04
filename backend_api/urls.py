from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from User import views
from job.views import JobPostviewset
from User.views import LoginView
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'user', views.UserProfileViewSet)
router.register(r'todo', views.TodoViewset)
router.register(r'job',JobPostviewset )
# router.register(r'login',LoginView )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path('api/logout/', obtain_auth_token, name='logout'),
    path('api/login/', LoginView.as_view(), name='login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
