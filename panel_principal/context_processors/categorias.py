from panel_principal.models import categorias_juegos

def lista_categorias(request):
    todas_categorias = {
        'categorias' : categorias_juegos.objects.all()
    }
    return todas_categorias