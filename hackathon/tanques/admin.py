from django.contrib import admin
from .models import Tanque

# Register your models here.
class Tanques(admin.ModelAdmin):
	"""docstring for Tanques"""
	list_display = ['nome', 'proprietario', 'especie']
	search_fields = ['nome', 'proprietario']
	prepopulated_fields = {'slug':('nome',)}


admin.site.register(Tanque, Tanques)