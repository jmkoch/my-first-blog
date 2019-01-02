from django.contrib import admin
from .models import Trait
from import_export.admin import ImportExportModelAdmin

#admin.site.register(Trait)

@admin.register(Trait)
class TraitAdmin(ImportExportModelAdmin):
	pass