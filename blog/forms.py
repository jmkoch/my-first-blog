#from django import forms
from .models import Post
from django.forms import ModelForm

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'n_floatNum', 'n_smallIntNum', 'n_boolVal', 'isi_val', )

'''
class MinValueValidator(BaseValidator):
    message = _('Ensure this value is greater than or equal to %(limit_value)s.')
    code = 'min_value'

    def compare(self, a, b):
        return a < b


class MaxValueValidator(BaseValidator):
    message = _('Ensure this value is less than or equal to %(limit_value)s.')
    code = 'max_value'

    def compare(self, a, b):
        return a > b
'''