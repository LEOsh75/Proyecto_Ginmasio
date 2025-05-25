from django.shortcuts import get_object_or_404, render, redirect
from .forms import RegistroUsuarioForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Clase, Reserva
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import PerfilUsuarioForm
from django.contrib.auth.models import User
from django.core.mail import send_mail


@login_required
def inicio(request):
    clases_disponibles = Clase.objects.all()
    reservas = Reserva.objects.filter(usuario=request.user)
    return render(request, 'usuarios/inicio.html', {
        'clases': clases_disponibles,
        'reservas': reservas
    })

@login_required
def reservar_clase(request, clase_id):
    clase = get_object_or_404(Clase, id=clase_id)

    if Reserva.objects.filter(usuario=request.user, clase=clase).exists():
        return render(request, 'usuarios/inicio.html', {
            'clases': Clase.objects.all(),
            'reservas': Reserva.objects.filter(usuario=request.user),
            'mensaje': 'Ya estás registrado en esta clase.'
        })

    if clase.cupos_disponibles > 0:
        Reserva.objects.create(usuario=request.user, clase=clase)
        clase.cupos_disponibles -= 1
        clase.save()
        return redirect('inicio')
    else:
        return render(request, 'usuarios/error_reserva.html', {'mensaje': 'No hay cupos disponibles para esta clase.'})

@login_required
def mis_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user)
    return render(request, 'usuarios/mis_reservas.html', {'reservas': reservas})

@login_required
def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)
    clase = reserva.clase
    clase.cupos_disponibles += 1
    clase.save()
    reserva.delete()
    return redirect('mis_reservas')
def quejas_sugerencias(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        # Aquí validas (puedes hacer validaciones básicas)

        asunto = f'Nueva Queja/Sugerencia de {nombre}'
        cuerpo = f'Correo: {email}\n\nMensaje:\n{mensaje}'

        try:
            send_mail(asunto, cuerpo, None, ['tu_correo_destino@gmail.com'])
            messages.success(request, '¡Gracias por tu mensaje! Lo hemos recibido.')
        except Exception as e:
            messages.error(request, 'Error al enviar el mensaje, por favor intenta más tarde.')

        return redirect('quejas_sugerencias')

    return render(request, 'usuarios/quejas_sugerencias.html')
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('login')