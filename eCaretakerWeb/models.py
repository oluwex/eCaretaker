from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core import validators

# Create your models here

class Users(AbstractBaseUser):
    first_name = models.CharField('First Name', max_length=30, blank=True)
    middle_name = models.CharField('Middle Name', max_length=30,blank=True)
    last_name = models.CharField('Last Name', max_length=30, blank=True)
    email = models.EmailField(
        'email address',
        help_text='Enter a valid email address',
        unique=True,db_index=True,
        validators=[
            validators.RegexValidator(
                r'(^[\w_.+-]+@[\w-]+\.[\w-.]+$)', 'Enter a valid username. This value may contain only '
                  'letters, numbers and @/./+/-/_ characters.'
        )],
        error_messages={
            'unique':'A user with that email address already exist'}
    )
    address = models.CharField('Address', max_length=80, blank=True)
    alternate_address = models.CharField('Alternate Address', max_length=80, blank=80)
    phone_No = models.CharField('Phone Number', max_length=20, blank=True,
         validators=[validators.RegexValidator(
             r'[\d]{11,}',
             'Phone Number must only consist of numbers and must be eleven or greater in length'
         )
         ], unique=True, error_messages={
            'unique': 'A user with that phone number already exists'
        }
    )
    gender = models.CharField(
        'Gender',
        help_text='Select your gender',
        choices=[
            ('male','Male'),
            ('female, Female')
        ]
    )
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    joined = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    role = models.CharField(
        'Role',
        choices=[
            ('tenant', 'Tenant'),
            ('landlord', 'Landlord')
        ]
    )

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

