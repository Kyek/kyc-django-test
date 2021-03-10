from typing import Dict, List, Optional
from django.db import models

from rest_framework import serializers

from .models import Profile, User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "birthdate", "gender",
                  "phone_number", "address", "uuid")
        read_only_fields = ("uuid", )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password", "profile")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(email=validated_data['email'],
                    username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        # Updating nested data
        user.profile.first_name = validated_data["profile"]["first_name"]
        user.profile.last_name = validated_data["profile"]["last_name"]
        user.profile.birthdate = validated_data["profile"]["birthdate"]
        user.profile.gender = validated_data["profile"]["gender"]
        user.profile.phone_number = validated_data["profile"]["phone_number"]
        user.profile.address = validated_data["profile"]["address"]
        user.profile.save()
        return user


def serializer_factory(model: models.Model, fields: List,
                       read_only_fields: List, extra: Optional[Dict]):

    """
    Creates a Serializer class with the fields and read_only fields given, the extra it's for a nested field, if needed
    """
    Meta = type('Meta', (object, ), {
        'model': model,
        'fields': fields,
        'read_only_fields': read_only_fields
    })
    serializer_fields = {"Meta": Meta}
    if extra:
        serializer_fields.update(extra)
    return type('ProfileUpdateSerializer', (serializers.ModelSerializer, ),
                serializer_fields)
