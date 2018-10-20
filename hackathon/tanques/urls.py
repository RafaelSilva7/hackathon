from django.urls import path, include
from . import views

#Cria-se um app_name para poder utilizá-lo como namespace no projeto
app_name = 'tanques'

urlpatterns = [
	path('list/', views.listTanques, name='tanques'),
	path('<int:id>/', views.idTanques, name='id_tanque'),
	path('new/', views.newTanques, name='new_tanque'),
	path('edit/<int:id>', views.editTanques, name='edit_tanque'),
]