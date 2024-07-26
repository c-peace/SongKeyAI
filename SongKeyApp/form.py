from django import forms

class UserForm(forms.Form):
    url = forms.CharField(label='Url', max_length=100)