from enum import Enum
from datetime import date, datetime
import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.signals import post_save
from django.dispatch import receiver


class Gender(Enum):
    FEMALE = "F"
    MALE = "M"


    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)


class Profile(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    birthdate = models.DateField(default=datetime.now)
    gender = models.CharField(max_length=1, choices=Gender.choices(), default=Gender.FEMALE.value)
    phone_number = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=128, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)
    instance.profile.save