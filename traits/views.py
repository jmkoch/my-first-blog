from django.views.generic import CreateView
from django.views.generic.edit import CreateView
from traits.models import Trait
from traits.models import Pub  #need to create pub so that can import from pub.models instead of traits.models

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from crispy_forms.helper import FormHelper

from django.http import HttpResponse
from traits.resources import TraitResource

from tablib import Dataset
import csv
from django.contrib.auth.models import User

# Trait view 
class TraitCreateView(CreateView):
	model = Trait
	fields = ('genus', 'species', 'isi', 'fruit_type')

class PubCreateView(CreateView):
    model = Pub
    fields = ('lastName', 'middleName', 'firstName', 'citekey', 'pub_type')

# code to export the trait csv data from admin (shows up as a button on admin Traits page)
def export_traits_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="traits_output.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'genus', 'species', 'isi', 'fruit type'])

    traits = Trait.objects.all().values_list('id', 'genus', 'species', 'isi', 'fruit_type')
    
    for trait in traits:
        writer.writerow(trait)

    return response