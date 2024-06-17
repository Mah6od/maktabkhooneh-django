from django.forms import forms

class NameForms(forms.Form):
    name = forms.CharField(max_length=255)