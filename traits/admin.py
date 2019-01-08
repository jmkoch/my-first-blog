from django.contrib import admin
from .models import Trait
from import_export.admin import ImportExportModelAdmin
from django import forms
from .forms import TraitForm
from .resources import TraitResource

@admin.register(Trait)
class TraitAdmin(ImportExportModelAdmin):
	list_display = ('genus', 'species', 'isi', 'fruit_type')
	form = TraitForm
	resource_class = TraitResource
    #pass

# This code goes along with commented block in forms.py; 
# it supplements my attempt to validate data prior to importing it thru admin but doesn't work

#admin.site.register(Trait)   
#	form = TraitForm
#	list_display = ('genus', 'species', 'isi', 'fruit_type')

#@admin.register(TraitAdmin)