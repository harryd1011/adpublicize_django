from django import forms
from datetime import date

class MyForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')}))


class LoginForm(forms.Form):
    email= forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
