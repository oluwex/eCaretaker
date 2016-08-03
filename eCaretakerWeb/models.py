from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from django.core import validators
from django.utils.translation import ugettext_lazy as _

# Create your models here

class Users(AbstractBaseUser):

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_CHOICES = [(GENDER_MALE, _('Male')), (GENDER_FEMALE, _('Female'))]

    ROLE_LANDLORD = 'landlord'
    ROLE_TENANT = 'tenant'
    ROLE_CHOICES = [(ROLE_LANDLORD, _('Landlord')), (ROLE_TENANT, _('Tenant'))]

    first_name = models.CharField(_('First Name'), max_length=30, blank=True)
    middle_name = models.CharField(_('Middle Name'), max_length=30,blank=True)
    last_name = models.CharField(_('Last Name'), max_length=30, blank=True)
    email = models.EmailField(
        _('email address'),
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
    address = models.CharField(_('Address'), max_length=80, blank=True)
    alternate_address = models.CharField(_('Alternate Address'), max_length=80, blank=80)
    phone_No = models.CharField(_('Phone Number'), max_length=20, blank=True,
         validators=[validators.RegexValidator(
             r'[\d]{11,}',
             'Phone Number must only consist of numbers and must be eleven or greater in length'
         )
         ], unique=True, error_messages={
            'unique': 'A user with that phone number already exists'
        }
    )
    gender = models.CharField(
        _('Gender'),
        help_text='Select your gender',
        max_length=1,
        choices=GENDER_CHOICES,
    )
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    joined = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    role = models.CharField(
        _('Role'),
        max_length=1,
        help_text='Please select your user role',
        choices=ROLE_CHOICES,
    )

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name_plural = _("users")

    def __str__(self):
        return self.email

# class UserRoles(models.Model):
#     userid = models.ForeignKey('Users', models.CASCADE)
#     roleid = models.ForeignKey('Roles', models.CASCADE)
