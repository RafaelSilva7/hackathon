from django.forms import ModelForm
from .models import Tanque


class FormularioTanque(ModelForm):
	
	class Meta:
		model = Tanque
		exclude = ('created_at', 'updated_at', 'slug')
