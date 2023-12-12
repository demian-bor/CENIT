from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView
from .models import Usuario
from .forms import formulario_registro
from django.contrib.auth import authenticate, login, logout

# Clase para el registro de usuarios
class registrar_usuario(CreateView):
    model = Usuario
    template_name = 'admin-user/registro.html'
    form_class = formulario_registro
    success_url = '../'
    failed_url = '../registrarse/'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'panel-principal/post-status.html', {'post_success' : True})

    def form_invalid(self, form):
        return render(self.request, 'panel-principal/post-status.html', {'post_success' : False})


# Clase para visualizar datos de usuario
class ver_usuario(DetailView):
    model = Usuario
    template_name = 'admin-user/info-usuario.html'


# Clase para editar datos de usuario
class editar_usuario(UpdateView):
    model = Usuario
    template_name = 'admin-user/editar-usuario.html'
    form_class = formulario_registro
    success_url = '../'
    failed_url = '../editar-usuario/'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'panel-principal/post-status.html', {'post_success' : True})

    def form_invalid(self, form):
        return render(self.request, 'panel-principal/post-status.html', {'post_success' : False})


# Funcion para logueo de sesion
def login_usuario(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('panel')
        else:
           return redirect('login')
    else:
        return render(request, 'admin-user/login.html')


# Funcion para cierre de sesion
def logout_usuario(request):
    logout(request)
    return redirect('login')





