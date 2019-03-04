import csv
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

from django.contrib.contenttypes.fields import GenericRelation

from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import InlineCheckboxes
from pub.models import Pub

# variables for validation: check for alphanumeric chars, alpha chars, and numeric chars, respectively
val_alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Error: only alphanumeric characters are allowed.')
val_alpha = RegexValidator(r'^[a-zA-Z]*$', 'Error: only alphabetic characters are allowed.')
val_numeric = RegexValidator(r'^[0-9]*$', 'Error: only numeric characters are allowed.')

class Trait(models.Model):
    # might implement the following 'Meta' class addition at some point (Sai had this)
    #class Meta:
    #    permissions = (
    #        ('view_trait', 'Can view trait'),
    #    )
    genus = models.CharField(max_length=50, null=True, blank=False, validators=[val_alpha])#help_text= 'Enter data if known. Expects str as input')
    species = models.CharField(max_length=50, null=True, blank=False, validators=[val_alpha])
    isi = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0, message='Must be a number between 0.0 and 1.0'), MaxValueValidator(1.0, message='Must be a number between 0.0 and 1.0')])
    
    FRUIT_TYPE_CHOICES = (('capsule','capsule'), ('CAPSULE', 'CAPSULE'), ('Capsule', 'Capsule'),('berry','berry'), ('Berry', 'Berry'), ('BERRY', 'BERRY')) # check why need doubles 
    fruit_type = models.CharField(max_length=50, null=False, default='none', choices=FRUIT_TYPE_CHOICES)
    publication = models.ForeignKey(Pub, on_delete=models.CASCADE, null=True)#, db_column='citekey')
# step 1: fix migrations to allow foreign key publication line (29 here) to work
# add trait --> citekey field should have something there: see what it looks like (does it list all pubs that 
# have been imported already? get a better sense of what's here)

# csv practice code below

#with open("/Users/JMK/traits-example_short.csv", mode = "r") as infile, open("traits-example_cleaned.csv", "r") as outfile:      reader = csv.reader(infile) #reading input csv file
#        next(reader, None) #skips headers
#        writer = csv.writer(outfile) #allows specified outfile to be written to
#        for row in reader: #iterating through rows in csv
#            Trait.objects.get_or_create(
#                isi=row[7],
#                fruit_type=row[21],
#                genus=row[1],
#                species=row[2],
#                )
            # get_or_create creates a tuple of the new object or
            # current object and a boolean of if it was created