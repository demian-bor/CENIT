from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView
from .forms import form_contacto, form_posteo, form_comentario, form_nueva_categoria
from .models import contacta_nos, categorias_juegos, posteos_usuarios, comentarios_usuarios
from django.db.models import Q


# Vista para la lista de publicaciones
class listar_publicaciones(ListView):
    model = posteos_usuarios
    template_name = 'main.html'
'''
# Vista para la lista de publicaciones
class listar_publicaciones(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posteos'] = posteos_usuarios.objects.all()
        context['categorias'] = categorias_juegos.objects.all()
        return context
'''

# Vista para el formulario de contacto
def contacto(request):
    form = form_contacto(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'contact.html', {'post_success' : True})
    else:
        return render(request, 'contact.html', {'post_success' : False, 'form' : form})


# Vista para la lista de publicaciones
class detalle_publicacion(DetailView):
    model = posteos_usuarios
    template_name = 'panel-principal/ver-post.html'


# Vista para la creacion de publicaciones
class postear_publicacion(CreateView):
    model = posteos_usuarios
    template_name = 'panel-principal/crear-post.html'
    form_class = form_posteo
    success_url = '../'
    failed_url = '../publicar/'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'panel-principal/crear-post.html', {'post_success' : True})

    def form_invalid(self, form):
        return render(self.request, 'panel-principal/crear-post.html', {'post_success' : False})


# Vista para la modificacion de publicaciones
class modificar_publicacion(UpdateView):
    model = posteos_usuarios
    template_name = 'panel-principal/actualizar.html'
    form_class = form_posteo
    success_url = '../'
    failed_url = '../actualizar/'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'panel-principal/post-status.html', {'post_success' : True})

    def form_invalid(self, form):
        return render(self.request, 'panel-principal/post-status.html', {'post_success' : False})


# Vista para el borrado de publicaciones
class eliminar_publicacion(DeleteView):
    model = posteos_usuarios
    template_name = 'panel-principal/eliminar.html'
    success_url = '../'


# Vista para la busqueda de publicaciones
def buscar_publicaciones(request):
    search_post = request.POST.get('search')
    if search_post:
        posts = posteos_usuarios.objects.filter(Q(post_title__icontains=search_post) | Q(post_subtitle__icontains=search_post) | Q(post_description__icontains=search_post))
    else:
        posts = posteos_usuarios.objects.all()
    return render(request, 'panel-principal/search.html', {'posts': posts})


# Vista para la busqueda de categorias
def buscar_categoria(request):
    search_post = request.GET.get('cat')
    posts = posteos_usuarios.objects.filter(post_category=search_post)
    return render(request, 'panel-principal/categoria.html', {'posts': posts})


# Vista para la pantalla principal
def about(request):
    return render(request, 'about.html', {})


