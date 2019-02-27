from django.contrib import admin
from pub.models import Pub,Person
# Register your models here.
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Pub)
admin.site.register(Person)