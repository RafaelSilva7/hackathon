from django.shortcuts import render
from django.http import HttpResponse


from .models import Tanque
from .forms import FormularioTanque

# Create your views here.
def listTanques(request):
	list_tanques = Tanque.objects.all()
	template = 'tanques/list.html'
	context = {
		'tanques' : list_tanques,
	}

	return render(request, template, context)

def idTanques(request, id):
	tanque = Tanque.objects.get(pk=id)
	template = 'tanques/show.html'
	context = {
		'tanques' : tanque,
	}

	return render(request, template, context)

def newTanques(request):
	if request.method == 'POST':
		new_tanque = FormularioTanque(request.POST)
		if new_tanque.is_valid():
			new_tanque.save()
			return HttpResponse("salvo")
	else:
		form_tanque = FormularioTanque()
	return render(request, 'tanques/new.html', {'form_tanque': form_tanque})

def editTanques(request, id):
	tanque = Tanque.objects.get(pk=id)

	if request.method == 'POST':
		form_tanque = FormularioTanque(request.POST, instance=tanque)
		if form_tanque.is_valid():
			tanque = form_tanque.save(commit=True)
			tanque.pk = id
			tanque.save()
			return HttpResponse("salvo") 
	else:
		form_tanque = FormularioTanque(instance=tanque)

	return render(request, 'tanques/edit.html', {'form_tanque': form_tanque, 'id': id})
