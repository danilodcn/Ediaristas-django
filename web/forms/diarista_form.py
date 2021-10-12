from django import forms
from ..models import Diarista
import re

class DiaristaForm(forms.ModelForm):
    cpf = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '000.000.000-00'}))
    cep = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '00000-000'}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '(00) 00000-0000'}))

    class Meta:
        model = Diarista
        fields = "__all__"

    def clean_cpf(self):
        cpf = self.cleaned_data["cpf"]
        return re.sub(r"\D", '', cpf)

    def clean_telefone(self):
        telefone = self.cleaned_data["telefone"]
        return re.sub(r'\D', '', telefone)

    def clean_cep(self):
        cep = self.cleaned_data["cep"]
        return re.sub(r'\D', '', cep)