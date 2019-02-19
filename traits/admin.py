from django.contrib import admin
from . import models
from .models import Trait
from import_export.admin import ImportExportModelAdmin
from django import forms
from .forms import TraitForm
from .resources import TraitResource

# registering the Trait model
@admin.register(Trait)
class TraitAdmin(ImportExportModelAdmin):
	# the line below displays labels to the admin Trait page so that users can see uploaded data
	list_display = ('id', 'genus', 'species', 'isi', 'fruit_type')
	form = TraitForm
	resource_class = TraitResource
    #pass