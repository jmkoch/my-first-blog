from django.db import models

from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import InlineCheckboxes

class Trait(models.Model):
    #class Meta:
    #    permissions = (
    #        ('view_trait', 'Can view trait'),
    #    )
    genus = models.CharField(max_length=50, null=True, blank=False, )#help_text= 'Enter data if known. Expects str as input')
    species = models.CharField(max_length=50, null=True, blank=False, )
    isi = models.FloatField(blank=True, null=True, )
    
    FRUIT_TYPE_CHOICES = (('Capsule','Capsule'),('Berry','Berry'))
    fruit_type = models.CharField(max_length=50, null=False, default='none', choices=FRUIT_TYPE_CHOICES)
