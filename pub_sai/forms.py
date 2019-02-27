from django import forms
from django.forms import ModelForm
from pub.models import  Pub, Person
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class BibtexForm(forms.Form):
    file_name = forms.FileField()


class PubForm(ModelForm):
    class Meta:
        model = Pub
        fields = ['type','address','annotate','lastName','middleName','firstName','booktitle','chapter','crossref',
            'edition','editor','howpublished','institution','journal',
            'citekey','month','note','number','organization','pages',
            'publisher','school','series','title','volume','year']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        #article, book, incollection, manual, misc, phdthesis, unpublished are some common types

        self.helper.layout = Layout(
            Fieldset(
                'Entry Type',
                'type',
                'citekey',
            ),
            Fieldset(
                'People',
                'lastName',
                'middleName',
                'firstName',
                'editor'
            ),

            Fieldset(
                'Fields',
                 'address', 'annotate', 'booktitle', 'chapter', 'crossref',
                 'edition', 'howpublished', 'institution', 'journal',
                 'month', 'note', 'number', 'organization', 'pages',
                 'publisher', 'school', 'series', 'title', 'volume', 'year'
            ),
            ButtonHolder(
                Submit('create', 'Create Pub', css_class='button white')
            )

        )
        super(PubForm, self).__init__(*args, **kwargs)


class PubUpdateForm(ModelForm):
    comment = forms.CharField(label="Update comment:",required=True)    #user needs to make a comment when updating fields
    class Meta:
        model = Pub
        fields = ['type','address','annotate','lastName','middleName','firstName','booktitle','chapter','crossref',
            'edition','editor','howpublished','institution','journal',
            'citekey','month','note','number','organization','pages',
            'publisher','school','series','title','volume','year']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        #article, book, incollection, manual, misc, phdthesis, unpublished are some common types

        self.helper.layout = Layout(
            Fieldset(
                'Update Comment',
                'comment',
            ),
            Fieldset(
                'Entry Type',
                'type',
                'citekey',
            ),
            Fieldset(
                'People',
                'lastName',
                'middleName',
                'firstName',
                'editor'
            ),

            Fieldset(
                'Fields',
                 'address', 'annotate', 'booktitle', 'chapter', 'crossref',
                 'edition', 'howpublished', 'institution', 'journal',
                 'month', 'note', 'number', 'organization', 'pages',
                 'publisher', 'school', 'series', 'title', 'volume', 'year'
            ),
            ButtonHolder(
                Submit('update', 'Update Pub', css_class='button white')
            )

        )
        super(PubUpdateForm, self).__init__(*args, **kwargs)


class PubSearchForm(ModelForm):
    class Meta:
        model = Pub
        fields = ['type','address','annotate','lastName','middleName','firstName','booktitle','chapter','crossref',
            'edition','editor','howpublished','institution','journal',
            'citekey','month','note','number','organization','pages',
            'publisher','school','series','title','volume','year']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        abstract = forms.CharField(required=False)
        address = forms.CharField(max_length=50, required=False)
        annotate = forms.CharField(max_length=50, required=False)
        #author = forms.ModelChoiceField(Person, required=False)
        lastName = forms.CharField(max_length=50, required=False)
        middleName = forms.CharField(max_length=50, required=False)
        firstName = forms.CharField(max_length=50, required=False)
        booktitle = forms.CharField(max_length=50, required=False)
        chapter = forms.CharField(max_length=50, required=False)
        crossref = forms.CharField(max_length=50, required=False)
        doi = forms.CharField(max_length=50, required=False)
        edition = forms.CharField(max_length=50, required=False)
        editor = forms.ModelChoiceField(Person, required=False)
        howpublished = forms.CharField(max_length=50, required=False)
        institution = forms.CharField(max_length=50, required=False)
        journal = forms.CharField(max_length=50, required=False)
        citekey = forms.CharField(max_length=50, required=False)
        keywords = forms.CharField(max_length=50, required=False)
        month = forms.CharField(max_length=50, required=False)
        note = forms.CharField(max_length=50,required=False)
        number = forms.CharField(max_length=50, required=False)
        organization = forms.CharField(max_length=50, required=False)
        pages = forms.CharField(max_length=50, required=False)
        publisher = forms.CharField(max_length=50, required=False)
        school = forms.CharField(max_length=50, required=False)
        series = forms.CharField(max_length=50, required=False)
        title = forms.CharField(max_length=50, required=False)
        TYPE_CHOICES = (('article', 'article'), ('book', 'book'), ('incollection','incollection'),
                        ('manual', 'manual'), ('misc', 'misc'),
                        ('unpublished', 'unpublished'))
        #type = forms.ModelChoiceField(max_length=50, required=False,choices=TYPE_CHOICES)
        type = forms.CharField(max_length=50, required=False)
        volume = forms.CharField(max_length=50, required=False)
        year = forms.CharField(max_length=50, required=False)
        url = forms.CharField(max_length=50, required=False)
        super(PubSearchForm, self).__init__(*args, **kwargs)
