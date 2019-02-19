from django.contrib import admin
from . import models
from .models import Trait, Person
from import_export.admin import ImportExportModelAdmin
from django import forms
from .forms import TraitForm #, MyCrispyForm
from .resources import TraitResource

# this register block works; just commenting out to test out below crispy attempt
@admin.register(Trait)
class TraitAdmin(ImportExportModelAdmin):
	list_display = ('id', 'genus', 'species', 'isi', 'fruit_type')
	form = TraitForm
	resource_class = TraitResource
    #pass


#class PersonAdmin(admin.ModelAdmin):
#	list_display = ('name', 'email', 'birth_date', 'location')

#admin.site.register(Person, PersonAdmin)




'''
# trying to incorporate crispy form into admin
@admin.register(models.Trait)
class TraitAdmin(admin.ModelAdmin):
	form = MyCrispyForm
	add_form_template = "traits/my_form.html"

# This code goes along with commented block in forms.py; 
# it supplements my attempt to validate data prior to importing it thru admin but doesn't work
'''

#admin.site.register(Trait)   
#	form = TraitForm
#	list_display = ('genus', 'species', 'isi', 'fruit_type')


#class TraitAdmin(ImportExportModelAdmin):
#	class Meta:
#	    list_display = ('genus', 'species', 'isi', 'fruit_type')
#	    form = TraitForm
#	    resource_class = TraitResource