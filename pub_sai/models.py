from django.db import models
from django.core.exceptions import ValidationError
#from django.utils.translation import gettext as _
from django.contrib.contenttypes.fields import GenericRelation
from usage_log.models import ChangeItem

#This is a manager to manage restricted operatinos
class RestrictedManager(models.Manager):
    ''' This manager filters out deleted sets'''
    def get_queryset(self):
        results = super(RestrictedManager, self).get_queryset().filter(safe_deleted=False)
        return results.filter(safe_deleted=False)
    def all_with_deleted(self):
        return super(RestrictedManager, self).get_queryset()
    def deleted_set(self):
        return super(RestrictedManager, self).get_queryset().filter(safe_deleted=True)

class Person(models.Model):
    first_names = models.CharField(max_length=100, null=True, blank=True)
    middle_names = models.CharField(max_length=100, null=True, blank=True)
    last_names = models.CharField(max_length=100, null=True, blank=True)

    #flag kept for safe deletion
    safe_deleted=models.BooleanField(null=False,default=False)

    objects = models.Manager()
    rmobjects = RestrictedManager()

    def __unicode__(self):
        name = ''
        if self.first_names!=None:
            name += str(self.first_names)
        if self.middle_names!=None:
            name += " "+str(self.middle_names)
        if self.last_names !=None:
            name += " "+ str(self.last_names)
        return name


    def __str__(self):
        name = ''
        if self.first_names!=None:
            name += str(self.first_names)
        if self.middle_names!=None:
            name += " "+str(self.middle_names)
        if self.last_names !=None:
            name += " "+ str(self.last_names)
        return name

    
class Pub(models.Model):
    abstract = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=100,null=True, blank=True)
    annotate = models.TextField( null=True, blank=True)
    #author = models.ManyToManyField(Person,related_name='author', null=True, blank=True)
    lastName = models.CharField(max_length=100, null=True, blank=True)
    middleName = models.CharField(max_length=100, null=True, blank=True)
    firstName = models.CharField(max_length=100, null=True, blank=True)
    booktitle = models.CharField(max_length=100, null=True, blank=True)
    chapter = models.CharField(max_length=100, null=True, blank=True)
    crossref = models.CharField(max_length=100, null=True, blank=True)
    doi = models.CharField(max_length=100, null=True, blank=True)
    edition = models.CharField(max_length=100, null=True, blank=True)
    editor = models.ManyToManyField(Person,related_name='editor', null=True, blank=True)
    howpublished = models.CharField(max_length=100, null=True, blank=True)
    institution = models.CharField(max_length=100, null=True, blank=True)
    journal = models.CharField(max_length=100, null=True, blank=True)
    citekey = models.CharField(max_length=100, blank=False, unique=True)
    keywords = models.CharField(max_length=100, null=True, blank=True)
    month = models.CharField(max_length=100, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    number = models.CharField(max_length=100, null=True, blank=True)
    organization = models.CharField(max_length=100, null=True, blank=True)
    pages = models.CharField(max_length=100, null=True, blank=True)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    school = models.CharField(max_length=100, null=True, blank=True)
    series = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=500, null=False, blank=True)
    TYPE_CHOICES = (('article','article'), ('book','book'),
                    ('incollection','incollection'), ('manual','manual'), ('misc','misc'),
                    ('unpublished', 'unpublished'))
    type = models.CharField(max_length=100, null=True, blank=True, choices=TYPE_CHOICES)
    volume = models.CharField(max_length=100, null=True, blank=True)
    year = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)


    #flag kept for safe deletion
    safe_deleted=models.BooleanField(null=False,default=False)

    #track change items
    change_items = GenericRelation(ChangeItem)

    objects = models.Manager()
    rmobjects = RestrictedManager()


    def __unicode__(self):
        return self.citekey

    def __str__(self):
        return self.citekey



