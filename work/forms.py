from django import forms
from .models import Garbages

class GarbageForm(forms.ModelForm):
    class Meta:
        model = Garbages
        fields = ['garbage_item', 'weight', 'description']
        exclude = ['request']
        widgets = {
            'garbage_item': forms.Select(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }