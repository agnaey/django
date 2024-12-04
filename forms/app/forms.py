from django import forms
from . models import student

class normal_form(forms.Form):
    roll_no=forms.IntegerField()
    name=forms.CharField()   
    age=forms.IntegerField()

class model_form(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'
