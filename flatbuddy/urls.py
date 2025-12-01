from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from user.views import UserViewSet, UserProfileViewSet, UserHousingViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('profiles', UserProfileViewSet)
router.register('housing', UserHousingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('blockchain/', include('blockchain.urls')),
]
