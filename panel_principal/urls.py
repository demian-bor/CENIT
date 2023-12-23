from django.urls import path
from . import views

urlpatterns = [
    path('', views.publicaciones_nuevas.as_view(), name='panel'),
    path('<int:pk>', views.detalle_publicacion.as_view(), name='ver-post'),
    path('todas', views.listar_publicaciones.as_view(), name='todas'),
    path('publicar', views.postear_publicacion.as_view(), name='publicar'),
    path('comentar', views.comentar_publicacion.as_view(), name='comentar'),
    path('actualizar/<int:pk>', views.modificar_publicacion.as_view(), name='actualizar'),
    path('eliminar/<int:pk>', views.eliminar_publicacion.as_view(), name='eliminar'),

    path('actualizar-comentario/<int:pk>', views.actualizar_comentario.as_view(), name='actualizar-comentario'),
    path('eliminar-comentario/<int:pk>', views.eliminar_comentario.as_view(), name='eliminar-comentario'),


    path('categoria', views.buscar_categoria, name='categoria'),
    path('buscar', views.buscar_publicaciones, name='buscar'),
    path('contacto', views.contacto, name='contacto'),
    path('nosotros', views.about, name='nosotros'),
]
