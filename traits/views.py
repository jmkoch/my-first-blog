from django.views.generic import CreateView
from traits.models import Trait, Person

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
#from .models import Post
#from .forms import PostForm
#from uni_form.helper import FormHelper
from crispy_forms.helper import FormHelper
from django.views.generic.edit import CreateView

from django.http import HttpResponse
from traits.resources import TraitResource #PostResource

from tablib import Dataset

import csv

from django.contrib.auth.models import User
#from traits.forms import AddressForm

class TraitCreateView(CreateView):
	model = Trait
	fields = ('genus', 'species', 'isi', 'fruit_type')

class PersonCreateView(CreateView):
	model = Person
	fields = ('name', 'email', 'birth_date', 'location')

def export(request):
    person_resource = PersonResource()
    TRAITdataset = person_resource.export()
    response = HttpResponse(PERSONdataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="PERSONposts.csv"'
    return response

def simple_upload(request):
    if request.method == 'POST': 
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True, raise_errors=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False, raise_errors=True)  # Actually import now

def before_import(self, dataset, dry_run, **kwargs):
    if 'id' not in dataset.headers:
        dataset.headers.append('id')

    return render(request, 'blog/simple_upload.html')

def export_traits_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="traits_output.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'genus', 'species', 'isi', 'fruit type'])

    traits = Trait.objects.all().values_list('id', 'genus', 'species', 'isi', 'fruit_type')
    
    for trait in traits:
        writer.writerow(trait)

    return response
#class AddressCreateView(CreateView):
#	fields = ('email', 'password', 'address_1', 'address_2', 'city', 'state', 'zip_code')