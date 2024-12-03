from django import forms

class normal_form(forms.Form):
    roll_no=forms.IntegerField()

    name=forms.CharField()
    
    age=forms.IntegerField()