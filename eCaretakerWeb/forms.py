from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Users

class Login(AuthenticationForm):
    class Meta:
        fields = [
            'username',
            'password',
        ]

class Register(UserCreationForm):
    # def __init__(self, request, *args, **kwargs):
    #     super(Register, self).__init__(*args, **kwargs)
    #     self.fields['last_name', 'first_name', 'middle_name', 'role'].required = True

    class Meta:
        model = Users
        fields = [
            'username',
            'last_name',
            'first_name',
            'middle_name',
            'email',
            'phone_No',
            'gender',
            'address',
            'alternate_address',
            'role',
        ]