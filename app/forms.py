from django import forms
from app.models import Proxylist

class ProxyForm(forms.ModelForm):
    class Meta:
        model = Proxylist
        exclude = ()


        widgets = {
            'ip_address' : forms.TextInput(attrs={'class' : 'form-control', 'autofocus' : '' }),
            'port' : forms.NumberInput(attrs={'class' : 'form-control' }),
            'protocol' : forms.TextInput(attrs={'class' : 'form-control'}),
            'anonymity' : forms.TextInput(attrs={'class' : 'form-control'}),
            'country' : forms.TextInput(attrs={'class' : 'form-control'}),
            'region' : forms.TextInput(attrs={'class' : 'form-control'}),
            'city' : forms.TextInput(attrs={'class' : 'form-control'}),
            'uptime' : forms.NumberInput(attrs={'class' : 'form-control' }),
            'response' : forms.NumberInput(attrs={'class' : 'form-control' }),
            'transfer' : forms.NumberInput(attrs={'class' : 'form-control' }),
        }