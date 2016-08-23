from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Complaints(models.Model):
    title = models.CharField(
        _('Title'),
        help_text='Enter the title of complaint',
        max_length=30,
        blank=False,
        null=True
    )
    body = models.TextField(
        _('Content'),
        help_text='Write complaint here',
        max_length=300,
        blank=True,
        null=False
    )