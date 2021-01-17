from django import forms
from .models import Flavor
from core.validators import validate_code

class FlavorForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["title"].validators.append(validate_code)
        
    class Meta: 
        model = Flavor
        fields = ['title','body']

