from django import forms
from.models import AnimalList


class DateInput(forms.DateInput):
    input_type = 'date'


class AnimalForm(forms.ModelForm):
    class Meta:
        model = AnimalList
        fields = ('animal', 'breed', 'date')
        widgets = {
            'animal': forms.Select(attrs={'class': 'form-select'}),
            'breed': forms.Select(attrs={'class': 'form-select'}),
            'date': DateInput(attrs={'class': 'form-control'}),
        }