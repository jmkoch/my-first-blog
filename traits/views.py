from django.views.generic import CreateView
from traits.models import Trait
#from traits.forms import AddressForm

class TraitCreateView(CreateView):
	model = Trait
	fields = ('genus', 'species', 'isi', 'fruit_type')

#class AddressCreateView(CreateView):
#	fields = ('email', 'password', 'address_1', 'address_2', 'city', 'state', 'zip_code')