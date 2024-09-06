from django import forms
from .models import *

class ItemInfo(forms.ModelForm):
    class Meta:
        model=Studentmodel
        fields='__all__'