from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import InlineCheckboxes

class Trait(models.Model):
    #class Meta:
    #    permissions = (
    #        ('view_trait', 'Can view trait'),
    #    )
    genus = models.CharField(max_length=50, null=True, blank=False, )#help_text= 'Enter data if known. Expects str as input')
    species = models.CharField(max_length=50, null=True, blank=False, )
    isi = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0, message='Must be a number between 0.0 and 1.0'), MaxValueValidator(1.0, message=None)])
    
    FRUIT_TYPE_CHOICES = (('Capsule','Capsule'),('Berry','Berry'))
    fruit_type = models.CharField(max_length=50, null=False, default='none', choices=FRUIT_TYPE_CHOICES)
