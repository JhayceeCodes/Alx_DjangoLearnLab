# myapp/forms.py
from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(widget=forms.Textarea)
    publication_year = forms.DateField()
