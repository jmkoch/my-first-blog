from django.db import models
# from traits.models import Trait this produces ImportError... why??

import csv
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import InlineCheckboxes

val_alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Error: only alphanumeric characters are allowed.')
val_alpha = RegexValidator(r'^[a-zA-Z]*$', 'Error: only alphabetic characters are allowed.')
val_numeric = RegexValidator(r'^[0-9]*$', 'Error: only numeric characters are allowed.')


class Pub(models.Model):
    lastName = models.CharField(max_length=50, null=True, blank=False, validators=[val_alpha])
    middleName = models.CharField(max_length=50, null=True, blank=False, validators=[val_alpha])
    firstName = models.CharField(max_length=50, null=True, blank=False, validators=[val_alpha])
    citekey = models.CharField(max_length=50, null=True, blank=False, unique=True, validators=[val_alphanumeric])
    
    PUB_TYPE_CHOICES = (('article', 'article'), ('book','book'))
    pub_type = models.CharField(max_length=50, null=True, blank=True, choices=PUB_TYPE_CHOICES)

    
    def __unicode__(self):
        return self.citekey

    def __str__(self):
        return self.citekey

    #trait_idMatch = models.ForeignKey('traits.Trait', on_delete=models.CASCADE,)