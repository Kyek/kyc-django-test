from rest_framework import routers

from .views import ProfileUpdateViewSet, UserCreateViewSet

app_name = "user_profile"

router = routers.DefaultRouter()

router.register("users", UserCreateViewSet, basename="users")
router.register("users/profile", ProfileUpdateViewSet, basename="profile")

urlpatterns = router.urls
