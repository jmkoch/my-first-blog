
from django.db import models

#from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
#from crispy_forms.bootstrap import InlineCheckboxes
#from crispy_forms.bootstrap import help_text_inline

class Foo(models.Model):
    """A magical creature from Foo dynasty"""
    mighty_name = models.CharField(max_length=255)
    kingdoms_count = models.PositiveIntegerField(default=0, help_text='how many?????')
    email = models.EmailField()