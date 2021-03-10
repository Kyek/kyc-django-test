from django.views.generic import base
from rest_framework import routers

from .views import UserCreateViewSet

app_name = "user_profile"

router = routers.DefaultRouter()

router.register("users", UserCreateViewSet, basename="users")

urlpatterns = router.urls