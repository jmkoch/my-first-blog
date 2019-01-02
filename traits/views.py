from django.views.generic import CreateView
from traits.models import Trait

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
#from traits.forms import AddressForm

class TraitCreateView(CreateView):
	model = Trait
	fields = ('genus', 'species', 'isi', 'fruit_type')

#class AddressCreateView(CreateView):
#	fields = ('email', 'password', 'address_1', 'address_2', 'city', 'state', 'zip_code')