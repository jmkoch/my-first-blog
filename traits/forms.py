from django import forms

from .models import Trait

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class TraitForm(forms.ModelForm):
    class Meta:
        model = Trait
        exclude = [id, ]
    def clean(self):
        genus = self.cleaned_data.get('genus')
        species = self.cleaned_data.get('species')
        isi = self.cleaned_data.get('isi')
        fruit_type = self.cleaned_data.get('fruit_type')
        if isi > 1.0:
            raise forms.ValidationError("ISI must be between 0.0 and 1.0")
        return self.cleaned_data

# the attempted admin crispy form (matches admin.py line 18 @register block)
'''class MyCrispyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-my-form'
        self.helper.form_class = 'my-form'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Trait
        fields = []
'''

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)