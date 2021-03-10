from django.db import models
from rest_framework import serializers

from .models import Profile, User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "birthdate", "gender",
                  "phone_number", "address")


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
        user.profile.first_name = validated_data["profile"]["first_name"]
        user.profile.last_name = validated_data["profile"]["last_name"]
        user.profile.birthdate = validated_data["profile"]["birthdate"]
        user.profile.gender = validated_data["profile"]["gender"]
        user.profile.phone_number = validated_data["profile"]["phone_number"]
        user.profile.address = validated_data["profile"]["address"]
        user.save()
        return user
