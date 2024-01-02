from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .forms import form_contacto, form_posteo, form_comentario
from .models import posteos_usuarios, comentarios_usuarios
from django.db.models import Q


# Vista para la lista de publicaciones en pantalla principal
class publicaciones_nuevas(ListView):
    model = posteos_usuarios
    template_name = 'main.html'

    # Obtener de la lista las primeras 10 publicaciones recientes
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['principales'] = posteos_usuarios.objects.all()[:10]
        return context


# Vista para la lista de todas las publicaciones
class listar_publicaciones(ListView):
    model = posteos_usuarios
    template_name = 'panel-principal/pub-todas.html'
    context_object_name = 'publicaciones'

    def get_queryset(self):
        queryset = super().get_queryset()
        # Obtener GET
        categoria_seleccionada = self.request.GET.get('category')
        orden_seleccionado = self.request.GET.get('sort-order')
        # Aplicar filtro
        if categoria_seleccionada:
            queryset = queryset.filter(post_category = categoria_seleccionada)
        if orden_seleccionado:
            if orden_seleccionado == 'ascendant':
                queryset = queryset.order_by('post_date')
            elif orden_seleccionado == 'descendant':
                queryset = queryset.order_by('-post_date')
        # devolver resultado filtrado y ordenado
        return queryset


# Vista para el formulario de contacto
def contacto(request):
    form = form_contacto(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'contact.html', {'post_success' : True})
    else:
        return render(request, 'contact.html', {'post_success' : False, 'form' : form})


# Vista para la lista detallada de publicaciones
class detalle_publicacion(DetailView):
    model = posteos_usuarios
    template_name = 'panel-principal/ver-post.html'

    # Obtener de la lista las primeras 10 publicaciones recientes
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = comentarios_usuarios.objects.filter(comment_related_post_id = self.object.post_id).order_by('-comment_date')
        return context


# Vista para la creacion de comentarios
class comentar_publicacion(CreateView):
    model = comentarios_usuarios
    template_name = 'panel-principal/comentar-post.html'
    form_class = form_comentario

    def form_valid(self, form):
        temporary_form = form.save(commit=False) # No se avanza con la publicacion
        temporary_form.comment_author_id = self.request.user.id
        temporary_form.comment_related_post_id = self.request.GET.get('post')
        return super().form_valid(temporary_form)

    def get_success_url(self):
        return reverse('ver-post', args=[self.request.GET.get('post')])


# Vista para la actualizacion de comentarios
class actualizar_comentario(UpdateView):
    model = comentarios_usuarios
    template_name = 'panel-principal/actualizar-comentario.html'
    form_class = form_comentario

    def get_success_url(self):
        return reverse('ver-post', args=[self.object.comment_related_post_id])


# Vista para el borrado de publicaciones
class eliminar_comentario(DeleteView):
    model = comentarios_usuarios
    template_name = 'panel-principal/eliminar.html'

    def get_success_url(self):
        return reverse('panel')


# Vista para la creacion de publicaciones
class postear_publicacion(CreateView):
    model = posteos_usuarios
    template_name = 'panel-principal/crear-post.html'
    form_class = form_posteo

    def form_valid(self, form):
        temporary_form = form.save(commit=False) # No se avanza con la publicacion
        temporary_form.post_author_id = self.request.user.id
        return super().form_valid(temporary_form)

    def get_success_url(self):
        #return render(self.request, 'panel-principal/crear-post.html', {'post_success' : True})
        return reverse('panel')


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


# Vista para mostrar la informacion acerca de nosotros
def about(request):
    return render(request, 'about.html', {})


