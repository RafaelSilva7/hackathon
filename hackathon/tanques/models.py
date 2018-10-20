from django.db import models
from usuarios.models import Proprietario
from peixes.models import Peixe

# Create your models here.
class Tanque(models.Model):
	'''
	'''
	nome = models.CharField('Name', max_length=250)
	proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE)
	numero_peixes = models.IntegerField('Número de Peixes')
	especie = models.ForeignKey(Peixe, on_delete=models.CASCADE)
	tamanho = models.FloatField('Tamanho do tanque (m3)')
	material = models.CharField('Material do tanque', max_length=150)

	manutencao = models.DateField('Data da Manutenção')

	#Imagens Vinculadas
	image = models.ImageField(upload_to='tanques/images', verbose_name='Imagem', null=True, blank=True)

	created_at = models.DateTimeField('Criado em', auto_now_add=True) 
	updated_at = models.DateTimeField('Atualizado em', auto_now=True) 

	slug = models.CharField('Atalho', max_length=250)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = 'Tanque'
		verbose_name_plural = 'Tanques'
		ordering = ['nome', 'proprietario']