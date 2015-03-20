__author__ = 'jc_mich'

from django import forms
from .models import Contacto, Grupo


class ContactoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ContactoForm, self).__init__(*args, **kwargs)
        self.fields['grupo'].queryset = Grupo.objects.filter(owner=user)

    class Meta:
        model = Contacto
        exclude = ['owner']


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        exclude = ['owner']


class LoginForm(forms.Form):
    usuario = forms.CharField(label="Usuario", widget=forms.TextInput())
    password = forms.CharField(label="Password", widget=forms.PasswordInput(render_value=False))
