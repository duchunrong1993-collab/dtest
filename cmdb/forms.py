from django import forms
from django.forms.widgets import TextInput
from .models import host

class hostForm(forms.ModelForm):
    class Meta:
        model = host
        exclude = ('id',)
        widgets = {
            'hostname': TextInput(attrs={'class': 'form-control'}),
            'ip': TextInput(attrs={'class': 'form-control'}),
            'disk': TextInput(attrs={'class': 'form-control'}),
            'cpu': TextInput(attrs={'class': 'form-control'}),
            'mem': TextInput(attrs={'class': 'form-control'}),
            'desc': TextInput(attrs={'class': 'form-control'}),
        }
