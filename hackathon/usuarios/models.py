from django.db import models


from django.contrib.auth.models import User


# Create your models here.

class Proprietario(models.Model):
	nome = models.CharField(max_length=100,default="",verbose_name="Nome do Proprietário")
	cpf = models.CharField(max_length=16,verbose_name="CPF do Proprietário")
	data_nascimento = models.DateField(verbose_name="Data de Nascimento")
	logradouro = models.CharField(max_length= 100,default='',verbose_name="Logradouro")
	cidade = models.CharField(max_length=45,default='',verbose_name='Cidade')
	estado = models.CharField(max_length=25,default='',verbose_name="Estado")
	cep = models.CharField(max_length=15,default='',verbose_name="CEP")
	#usuario = models.OneToOneField(User,on_delete=models.CASCADE) # Dá problema no SQLite

	def __str__(self):
		return self.nome

	class Meta:

		verbose_name = "Proprietário"
		verbose_name_plural = "Proprietários"


