from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class RealUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_CHOICES = [(GENDER_MALE, _('Male')), (GENDER_FEMALE, _('Female'))]

    ROLE_LANDLORD = 'landlord'
    ROLE_TENANT = 'tenant'
    ROLE_CHOICES = [(ROLE_LANDLORD, _('Landlord')), (ROLE_TENANT, _('Tenant'))]

    middle_name = models.CharField(_('Middle Name'), max_length=30, blank=False)
    address = models.TextField(_('Address'), max_length=80, blank=False)
    alternate_address = models.TextField(_('Alternate Address'), max_length=80, blank=80)
    phone_No = models.CharField(_('Phone Number'), max_length=20, blank=True,
                                validators=[validators.RegexValidator(
                                    r'(^[\d]{5,20})',
                                    'Phone Number must only consist of numbers and must be five or greater in length'
                                )
                                ], unique=True, error_messages={
            'unique': 'A user with that phone number already exists'
        }
                                )
    gender = models.CharField(
        _('Gender'),
        help_text='Select your gender',
        max_length=6,
        choices=GENDER_CHOICES,
    )
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    role = models.CharField(
        _('Role'),
        max_length=8,
        help_text='Please select your user role',
        choices=ROLE_CHOICES,
    )

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name_plural = _("users")

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s %s' % (self.user.first_name, self.middle_name, self.user.first_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name
