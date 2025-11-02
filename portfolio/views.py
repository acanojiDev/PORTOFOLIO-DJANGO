from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Perfil, Habilidad, Trabajo, Curriculum
from .forms import ContactoForm


def inicio(request):
    perfil = Perfil.objects.first()
    trabajos_list = Trabajo.objects.all()
    habilidades = Habilidad.objects.all()
    tecnologias_circulo = Habilidad.objects.filter(mostrar_en_circulo=True)
    curriculum_items = Curriculum.objects.all()
    
    habilidades_por_categoria = {}
    for habilidad in habilidades:
        categoria = habilidad.categoria
        if categoria not in habilidades_por_categoria:
            habilidades_por_categoria[categoria] = []
        habilidades_por_categoria[categoria].append(habilidad)
    
    form = None
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            mensaje = form.save()
            
            try:
                send_mail(
                    subject=f'Portfolio - Nuevo mensaje: {mensaje.asunto}',
                    message=f'''
Nombre: {mensaje.nombre}
Email: {mensaje.email}

Mensaje:
{mensaje.mensaje}
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else mensaje.email,
                    recipient_list=[perfil.email if perfil else 'admin@example.com'],
                    fail_silently=False,
                )
            except Exception as e:
                pass
            
            messages.success(request, '¡Gracias por tu mensaje! Te responderé pronto.')
            return redirect('/#contacto')
    else:
        form = ContactoForm()
    
    context = {
        'perfil': perfil,
        'trabajos': trabajos_list,
        'habilidades_por_categoria': habilidades_por_categoria,
        'tecnologias_circulo': tecnologias_circulo,
        'curriculum_items': curriculum_items,
        'form': form,
    }
    return render(request, 'portfolio/inicio_unico.html', context)


def trabajos(request):
    trabajos_list = Trabajo.objects.all()
    
    tipo_filtro = request.GET.get('tipo')
    if tipo_filtro:
        trabajos_list = trabajos_list.filter(tipo=tipo_filtro)
    
    context = {
        'trabajos': trabajos_list,
        'tipo_filtro': tipo_filtro,
    }
    return render(request, 'portfolio/trabajos.html', context)


def trabajo_detalle(request, trabajo_id):
    try:
        trabajo = Trabajo.objects.get(id=trabajo_id)
        trabajos_relacionados = Trabajo.objects.filter(
            tipo=trabajo.tipo
        ).exclude(id=trabajo_id)[:3]
    except Trabajo.DoesNotExist:
        messages.error(request, 'El trabajo solicitado no existe.')
        return redirect('trabajos')
    
    context = {
        'trabajo': trabajo,
        'trabajos_relacionados': trabajos_relacionados,
    }
    return render(request, 'portfolio/trabajo_detalle.html', context)


def acerca_de(request):
    perfil = Perfil.objects.first()
    habilidades = Habilidad.objects.all()
    
    habilidades_por_categoria = {}
    for habilidad in habilidades:
        categoria = habilidad.categoria
        if categoria not in habilidades_por_categoria:
            habilidades_por_categoria[categoria] = []
        habilidades_por_categoria[categoria].append(habilidad)
    
    context = {
        'perfil': perfil,
        'habilidades_por_categoria': habilidades_por_categoria,
    }
    return render(request, 'portfolio/acerca_de.html', context)


def contacto(request):
    perfil = Perfil.objects.first()
    
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            mensaje = form.save()
            
            try:
                send_mail(
                    subject=f'Portfolio - Nuevo mensaje: {mensaje.asunto}',
                    message=f'''
Nombre: {mensaje.nombre}
Email: {mensaje.email}

Mensaje:
{mensaje.mensaje}
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else mensaje.email,
                    recipient_list=[perfil.email if perfil else 'admin@example.com'],
                    fail_silently=False,
                )
            except Exception as e:
                pass
            
            messages.success(request, '¡Gracias por tu mensaje! Te responderé pronto.')
            return redirect('contacto')
    else:
        form = ContactoForm()
    
    context = {
        'perfil': perfil,
        'form': form,
    }
    return render(request, 'portfolio/contacto.html', context)

