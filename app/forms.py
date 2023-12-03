from django import forms

from .models import Veiculo, Visitante, Carga

class VeiculoModelForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'

class VisitanteModelForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = '__all__'

class CargaModelForm(forms.ModelForm):
    class Meta:
        model = Carga
        fields = '__all__'