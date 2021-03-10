from django.views.generic import base
from rest_framework import routers

from .views import UserCreateViewSet, ProfileUpdateViewSet

app_name = "user_profile"

router = routers.DefaultRouter()

router.register("users", UserCreateViewSet, basename="users")
router.register("users/profile", ProfileUpdateViewSet, basename="profile")

urlpatterns = router.urls