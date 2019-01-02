from import_export import resources
from .models import Person #Post

class PersonResource(resources.ModelResource): #PostResource
    class Meta:
        model = Person #Post