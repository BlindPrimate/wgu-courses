from django import forms
from .models import Degree


class DegreeComparerForm(forms.ModelForm):
    degrees = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Degree.objects.all()
    )
    class Meta:
        model = Degree
        fields = []
        

