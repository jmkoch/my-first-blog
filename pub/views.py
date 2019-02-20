from django.views.generic import CreateView
from django.views.generic.edit import CreateView
from pub.models import Pub

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from crispy_forms.helper import FormHelper

from django.http import HttpResponse
from pub.resources import PubResource

from tablib import Dataset
import csv
from django.contrib.auth.models import User

# Trait view 
class PubCreateView(CreateView):
	model = Pub
	fields = ('lastName', 'middleName', 'firstName', 'citekey', 'pub_type')
