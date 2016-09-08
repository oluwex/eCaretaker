from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import RealUsers


class LoginForm(AuthenticationForm):
    class Meta:
        fields = [
            'username',
            'password',
        ]


class Register(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'last_name',
            'first_name',
            'email',
        ]


class Register2(forms.ModelForm):
    class Meta:
        model = RealUsers
        fields = [
            'middle_name',
            'gender',
            'address',
            'phone_No',
            'alternate_address',
            'role',
        ]

class Edit(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'last_name',
            'first_name',
            'email',
            # 'middle_name',
            # 'gender',
            # 'address',
            # 'phone_No',
            # 'alternate_address',
            # 'role',
        ]


class ProfileForm(forms.Form):
    username = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    middle_name = forms.CharField(max_length=20)
