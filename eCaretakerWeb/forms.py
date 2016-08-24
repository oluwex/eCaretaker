from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import RealUsers, User
from eCaretakerLocations.models import House


class Login(AuthenticationForm):
    class Meta:
        fields = [
            'username',
            'password',
        ]


class Register(UserCreationForm):
    class Meta:
        model = RealUsers
        fields = [
            'middle_name',
            'phone_No',
            'gender',
            'address',
            'alternate_address',
            'role',
        ]

class Register2(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'last_name',
            'first_name',
            'email',
        ]