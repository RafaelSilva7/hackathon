from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from peixes.models import Peixe

def index(request):
	template = 'core/index.html'
	list_peixes = Peixe.objects.all()
	quant = len(list_peixes)

	#while (len(list_peixes)%4 != 0):
	#	list_peixes.insert(Peixe())
	print(len(list_peixes))
	context = {
		'list_peixes' : list_peixes,
	}
	return render(request, template, context)
