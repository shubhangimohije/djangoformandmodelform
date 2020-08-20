from django import forms
from .models import Student, University

class StudentForm(forms.Form):
    sid = forms.IntegerField()
    name = forms.CharField(max_length=70)
    email = forms.EmailField(max_length=70)

class UniversityForm(forms.ModelForm):
    class Meta:
        model= University
        fields='__all__'