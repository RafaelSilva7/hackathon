from django.urls import path
from . import views

app_name="usuarios"

urlpatterns = [

	path('cadastro/', views.criar_usuario, name="cadastrar_usuario"),
	path('login/', views.login_usuario, name="login_usuario"),
	path('logout/',views.logout_usuario,name="logout_usuario"),

]