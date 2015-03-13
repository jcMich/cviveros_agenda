__author__ = 'jc_mich'

from django import forms
from .models import Contacto, Grupo, Color


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        exclude = ['owner']


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
