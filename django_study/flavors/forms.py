from django import forms
from .models import Flavor

class FlavorForm(forms.ModelForm):
    class Meta: 
        model = Flavor
        fields = ['title','body']