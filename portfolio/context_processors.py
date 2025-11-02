from .models import Perfil


def perfil_global(request):
    try:
        perfil = Perfil.objects.first()
    except Perfil.DoesNotExist:
        perfil = None
    
    return {'perfil': perfil}

