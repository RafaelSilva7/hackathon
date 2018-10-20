from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from django.core.exceptions import ObjectDoesNotExist



from django.contrib.auth.decorators import login_required
from .models import Peixe

from .forms import FormularioPeixe
# Create your views here.

def mostrar_peixe(request, id_peixe):
	peixe = Peixe.objects.get(id=id_peixe)
	template = 'peixes/show.html'
	context = { 'peixe' : peixe }
	return render(request, template, context)


"View Para Criação de Peixes"
@login_required(login_url="usuarios/login/")
def criar_peixe(request):
	if request.method == 'GET':
		formulario_peixe = FormularioPeixe()
		contexto = {'formulario_peixe' : formulario_peixe}
		return render(request,'peixes/criar_peixe.html',contexto)

	else:
		formulario_peixe = FormularioPeixe(request.POST)
		if formulario_peixe.is_valid():
			novo_peixe = formulario_peixe.save(commit=False)
			novo_peixe.save()
			return HttpResponse("Salvo")
		contexto = {"formulario_peixe":formulario_peixe}
		return render(request,'peixes/criar_peixe.html',contexto)


"View para a edição de informações dos peixes"
@login_required(login_url="usuarios/login/")
def editar_peixe(request,id_peixe):
	if request.method == 'GET':
		peixe = Peixe.objects.get(id=id_peixe)
		formulario_peixe = FormularioPeixe(instance=peixe)
		contexto = {'formulario_peixe':formulario_peixe, 'peixe':peixe}
		return render(request,'peixes/editar_peixe.html',contexto)
	else:
		peixe = Peixe.objects.get(id=id_peixe)
		formulario_peixe = FormularioPeixe(instance=peixe, data=request.POST)
		if formulario_peixe.is_valid():
			formulario_peixe.save()
			return HttpResponse('Editado')
		contexto = {'formulario_peixe':formulario_peixe}
		return render(request,'peixes/editar_peixe.html',contexto)

