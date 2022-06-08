from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UsernameField

from core.models import User


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "avatar"
        ]


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}
