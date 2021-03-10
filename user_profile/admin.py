from typing import Any

from django.contrib import admin
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    invalid_first_name = forms.BooleanField(required=False)
    invalid_last_name = forms.BooleanField(required=False)
    invalid_birthdate = forms.BooleanField(required=False)
    invalid_phone_number = forms.BooleanField(required=False)
    invalid_address = forms.BooleanField(required=False)

    class Meta:
        model = Profile
        fields = [
            "owner",
            "first_name",
            "last_name",
            "birthdate",
            "gender",
            "phone_number",
            "address",
            "invalid_first_name",
            "invalid_last_name",
            "invalid_birthdate",
            "invalid_phone_number",
            "invalid_address",
        ]

    def save(self, commit: bool) -> Any:
        """
        Overrided save for setting fields to None
        """
        instance = super().save(commit=commit)
        for key, invalid in self.cleaned_data.items():
            if invalid:
                setattr(instance, key[8:], None)
        instance.save()
        return instance


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm
    readonly_fields = [
        "owner",
        "first_name",
        "last_name",
        "birthdate",
        "gender",
        "phone_number",
        "address",
    ]
    fieldsets = ((None, {
        "fields":
        ("owner", "first_name", "invalid_first_name", "last_name",
         "invalid_last_name", "birthdate", "invalid_birthdate", "phone_number",
         "invalid_phone_number", "address", "invalid_address")
    }), )
