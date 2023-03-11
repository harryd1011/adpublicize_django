from django import forms
from datetime import date

class MyForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')}))
