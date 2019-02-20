from django import forms
from .models import Pub

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class PubForm(forms.ModelForm):
    class Meta:
        model = Pub
        exclude = [id, ]
    def clean(self):
        lastName = self.cleaned_data.get('lastName')
        middleName = self.cleaned_data.get('middleName')
        firstName = self.cleaned_data.get('firstName')
        citekey = self.cleaned_data.get('citekey')
        pub_type = self.cleaned_data.get('pub_type')