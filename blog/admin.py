from django.contrib import admin
from .models import Post, Person
from import_export.admin import ImportExportModelAdmin

admin.site.register(Post)

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
	pass