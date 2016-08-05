from django.db import models
from eCaretakerWeb.models import Users
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class House(models.Model):
    name = models.CharField(
        _('House Name'),
        max_length=20,
        help_text="Leave blank if your house has no name yet",
        blank=True,
    )

    house_no = models.CharField(
        _('House No/Description'),
        max_length=20,
        help_text='Write your house number or any other description',
        blank=True,
    )

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    updated_time = models.DateTimeField(auto_now=True, auto_now_add=False)

    street = models.ForeignKey('Street', models.CASCADE, verbose_name='Street Name')

    city = models.ForeignKey('City', models.CASCADE, verbose_name='City')

    local_government = models.ForeignKey('LGA', models.CASCADE, verbose_name='Local Government')

    owner = models.ForeignKey(Users, models.CASCADE, verbose_name='owner')

    class Meta:
        verbose_name_plural = _('Houses')

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(
        _('Street Name'),
        max_length=50,
        blank=True,
    )

    timestamp = models.DateTimeField()

    city = models.ForeignKey('City', models.CASCADE, verbose_name="City")

    local_government = models.ForeignKey('LGA', models.CASCADE, verbose_name='Local Government Area')

    state = models.ForeignKey('State', models.CASCADE, verbose_name='State')


class City(models.Model):
    name = models.CharField(
        _('City Name'),
        max_length=30,
        blank=True,
    )

    local_government = models.ForeignKey('LGA', models.CASCADE, verbose_name='Local Government Area')

    state = models.ForeignKey('State', models.CASCADE, verbose_name='State')

    class Meta:
        verbose_name_plural = _('Cities')


    def __str__(self):
        return self.name


class LGA(models.Model):
    name = models.CharField(
        _('Local Government Area'),
        help_text='Please enter the name of the local government',
        max_length=30,
        blank=True,
    )

    stateId = models.ForeignKey('State', models.CASCADE,
                                verbose_name='state',
                                help_text='Please select the local government area state',)

    def __str__(self):
        return "%s" % self.name


class State(models.Model):
    name = models.CharField(
        _('name'),
        unique=True,
        help_text='Please enter the name of the state',
        max_length=30,
        blank=True
    )

    def __str__(self):
        return '%s' % self.name

    class meta:
        verbose_name = _('state'),
        verbose_name_plural = _('states')