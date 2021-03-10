from rest_framework import exceptions, mixins, serializers, views, viewsets
from rest_framework import permissions
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from drf_yasg.utils import swagger_auto_schema

from .models import User, Profile
from .permissions import OwnProfilePermission
from .serializers import UserSerializer, serializer_factory


class UserCreateViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def check_permissions(self, request):
        if not self.request.method == "POST":
            return super().check_permissions(request)

    def perform_create(self, serializer):
        serializer.save()


class ProfileUpdateViewSet(viewsets.GenericViewSet, mixins.UpdateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = None
    permission_classes = [IsAuthenticated, OwnProfilePermission]
    fields_to_validate = [
        "first_name", "last_name", "birthdate", "gender", "phone_number",
        "address"
    ]

    def get_serializer(self, *args, **kwargs):
        instance = args[0]
        read_only_profile_fields = []
        for field in self.fields_to_validate:
            current_value = getattr(instance, field)
            if current_value is not None:
                read_only_profile_fields.append(field)

        serializer_class = serializer_factory(Profile, self.fields_to_validate, read_only_profile_fields, None)

        self.serializer_class = serializer_class

        return super().get_serializer(*args, **kwargs)