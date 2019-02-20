from django.contrib import admin
from . import models
from .models import Pub
from import_export.admin import ImportExportModelAdmin
from django import forms
from .forms import PubForm
from .resources import PubResource

@admin.register(Pub)
class PubAdmin(ImportExportModelAdmin):
	# the line below displays labels to the admin Trait page so that users can see uploaded data
	list_display = ('lastName', 'middleName', 'firstName', 'citekey', 'pub_type')
	form = PubForm
	resource_class = PubResource