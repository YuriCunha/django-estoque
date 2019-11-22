# forms.py
from django import forms
from .models import Cores

class FormCores(forms.ModelForm):
    class Meta:
        model = Cores
        fields = ['cor', 'slug']