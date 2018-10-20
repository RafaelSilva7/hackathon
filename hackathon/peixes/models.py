from django.db import models

# Create your models here.



class Peixe(models.Model):
	TIPO_RACOES = ( ('Farelada','Farelada') , ('Peletizada','Peletizada') , ('Extrusada','Extrusada') )
	FASES_PEIXE = ( (1,'Alevinos') , (2,'Recria') , (3,'Engorda') )
	nome_especie = models.CharField(max_length=64, default="", verbose_name="Nome da Espécie de Peixe")
	tempo_medio_crescimento = models.PositiveIntegerField(default=0, verbose_name="Tempo Médio de Crescimento(Anos)")
	tipo_racoes = models.CharField(max_length=10, default="Farelada", choices=TIPO_RACOES, verbose_name="Tipo de Ração")
	espaco_ocupacao =  models.FloatField(default=0, verbose_name="Espaço de Ocupação em M²")
	quantidade_racao = models.FloatField(default=0, verbose_name="Quantidade de Ração")
	data_adicao = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Data de Adição")
	fase_atual = models.IntegerField(default=1,choices=FASES_PEIXE,verbose_name="Fase Atual de Criação")
	descricao = models.CharField(max_length=150, verbose_name='Breve Descricao')
	distrib_geograf = models.TextField(verbose_name='Distribuição Geográfica')
	caracteristica = models.TextField(verbose_name='Característica')
	reproducao = models.TextField(verbose_name='Reprodução')

	#Imagens Vinculadas
	image = models.ImageField(upload_to='peixes/images', verbose_name='Imagem', null=True, blank=True)

	def __str__(self):
		return self.nome_especie

	class Meta:
		verbose_name="Peixe"
		verbose_name_plural = "Peixes"



	