from django.urls import path
from .views import registrar_usuario, ver_usuario, editar_usuario, logout_usuario, login_usuario

urlpatterns = [
    path('login', login_usuario, name='login'),
    path('logout', logout_usuario, name='logout'),
    path('registrarse', registrar_usuario.as_view(), name='registrarse'),
    path('usuario/<int:pk>', ver_usuario.as_view(), name='usuario'),
    path('editar-usuario/<int:pk>', editar_usuario.as_view(), name='editar-usuario'),
]
