#from django import forms
from .models import Post #, Trait
from django.forms import ModelForm

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'n_floatNum', 'n_smallIntNum', 'n_boolVal', 'isi_val', )
'''
class TraitForm(ModelForm):
    class Meta:
        model = Trait
        fields = ['genus', 'species', 'fruit_type']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Taxonomy',
                'genus',
                'species',
            ),
            Fieldset(
                'Fruit Traits',
            InlineCheckboxes('fruit_type'),
            ),
            ButtonHolder(
                Submit('create', 'Create Trait', css_class='button white')
            )
        )

        super(TraitForm, self).__init__(*args, **kwargs)

'''
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