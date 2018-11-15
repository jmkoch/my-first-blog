from django.views.generic import CreateView
from traits.models import Trait

class TraitCreateView(CreateView):
	model = Trait
	fields = ('genus', 'species', 'isi', 'fruit_type')