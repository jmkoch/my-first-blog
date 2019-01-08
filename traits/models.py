import csv
from django.db import models
from django.utils import timezone
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
    isi = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0, message='Must be a number between 0.0 and 1.0'), MaxValueValidator(1.0, message='Must be a number between 0.0 and 1.0')])
    #if float(isi) < 0.0:
    #   raise ValidationError
    #if isi > 1.0:
    #    raise ValidationError
    
    FRUIT_TYPE_CHOICES = (('Capsule','Capsule'),('Berry','Berry'))
    fruit_type = models.CharField(max_length=50, null=False, default='none', choices=FRUIT_TYPE_CHOICES)

class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)
'''
with open("/Users/JMK/traits-example_short.csv", mode = "r") as infile, open("traits-example_cleaned.csv", "r") as outfile:
        reader = csv.reader(infile) #reading input csv file
        next(reader, None) #skips headers
        writer = csv.writer(outfile) #allows specified outfile to be written to
        for row in reader: #iterating through rows in csv
            Trait.objects.get_or_create(
                isi=row[7],
                fruit_type=row[21],
                genus=row[1],
                species=row[2],
                )
            # get_or_create creates a tuple of the new object or
            # current object and a boolean of if it was created
'''