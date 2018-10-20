from django.urls import path
from . import views


app_name="peixes"



urlpatterns = [
	path('criar/',views.criar_peixe, name="criar_peixe"),
	path('editar/<int:id_peixe>/', views.editar_peixe, name="editar_peixe" ),
	path('visualizar/<int:id_peixe>/', views.mostrar_peixe, name="mostrar_peixe"),
]