from django.db import models

# Create your models here.


class LGA(models.Model):
    name = models.CharField(
        ('Local Government Area'),
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
        ('name'),
        unique=True,
        help_text='Please enter the name of the state',
        max_length=30,
        blank=True
    )

    def __str__(self):
        return '%s' % self.name

    class meta:
        verbose_name = 'state',
        verbose_name_plural = 'states'
