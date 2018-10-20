from django.shortcuts import render,reverse

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect

from .forms import FormularioCadastroUsuario,FormularioLoginUsuario
# Create your views here.

def criar_usuario(request):

	if request.method=='GET':
		formulario_usuario = FormularioCadastroUsuario()
		contexto = { 'formulario_usuario' : formulario_usuario } 
		return render(request,'usuarios/cadastro_usuario.html',contexto)

	else:
		formulario_usuario = FormularioCadastroUsuario(request.POST)
		if formulario_usuario.is_valid():
			nome_usuario = request.POST['username']
			senha = request.POST['password']
			email = request.POST['email']
			usuario = User.objects.create_user(username=nome_usuario,password=senha,email=email)
			return HttpResponseRedirect(reverse(''))
		else:
			contexto = {formulario_usuario:formulario_usuario}
			return render(request, 'usuarios/cadastro_usuario.html', contexto)




def login_usuario(request):
	if request.method == 'GET':
		formulario_usuario = FormularioLoginUsuario()
		contexto = { 'formulario_usuario' : formulario_usuario }
		return render(request,'usuarios/login_usuario.html',contexto)
	
	else:
			nome_usuario = request.POST['username']
			senha = request.POST['password']
			usuario_autenticado = authenticate(username=nome_usuario,password=senha)
			if usuario_autenticado is not None:
				login(request,usuario_autenticado)
				return HttpResponse('Usuário Logado')	
			formulario_usuario = FormularioLoginUsuario()
			contexto = { 'formulario_usuario' : formulario_usuario }
			return render(request,'usuarios/login_usuario.html',contexto)



def logout_usuario(request):
	logout(request)
	return HttpResponseRedirect(reverse('core:index')) 


 
	