from django.forms import ModelForm

from .models import Peixe



'''Criação do Formulário da Classe Peixe'''
class FormularioPeixe(ModelForm):
	
	class Meta:
		model = Peixe
		fields = ('__all__')



