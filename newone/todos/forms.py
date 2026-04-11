from django import forms

class PersonForm(forms.Form):
     name = forms.CharField(max_length=100,label="Name")
     age = forms.IntegerField(label="age")
     job =forms.CharField(label="job",required=False)