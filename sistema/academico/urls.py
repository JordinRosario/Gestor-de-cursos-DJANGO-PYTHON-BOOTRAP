from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('registrarcurso/', views.registrar_curso, name='registrar_curso'),
    path('editarcurso/<codigo>', views.editar_curso),
    path('edicioncurso/', views.edicion_curso, name= 'edicion_curso'),
    path('eliminarcurso/<codigo>', views.eliminar_curso),
    
    #Register
    path('registrarte/', views.registrarte, name='registrarte'),
    path('iniciarsesion/', views.iniciar_sesion, name = 'iniciarsesion'),
    path('cerrarsesion/', views.cerrar_sesion, name = 'cerrarsesion')
]
