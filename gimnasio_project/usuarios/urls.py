from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('reservar/<int:clase_id>/', views.reservar_clase, name='reservar_clase'),
    path('mis_reservas/', views.mis_reservas, name='mis_reservas'),
    path('cancelar_reserva/<int:reserva_id>/', views.cancelar_reserva, name='cancelar_reserva'),
        path('quejas-sugerencias/', views.quejas_sugerencias, name='quejas_sugerencias'),

]
