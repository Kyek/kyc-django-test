from rest_framework import exceptions, mixins, serializers, viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from .models import User, Profile
from .serializers import UserSerializer


class UserCreateViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    authentication_classes = []
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
