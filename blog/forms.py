from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'n_floatNum', 'n_smallIntNum', 'n_boolVal', )