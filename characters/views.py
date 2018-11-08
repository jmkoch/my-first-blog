
from django.views.generic.edit import CreateView
from characters.models import Foo

class CreateFooView(CreateView):
    """A create view for Foo model"""
    model = Foo
    fields = ('mighty_name', 'kingdoms_count', 'email')
    template_name = "characters/create_foo.html"