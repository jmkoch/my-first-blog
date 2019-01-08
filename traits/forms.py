from django import forms

from .models import Trait

# I tried to add a form to be able to validate 
# data before importing but it didn't work

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