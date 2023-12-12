from django.contrib import admin
from .models import contacta_nos, categorias_juegos, posteos_usuarios, comentarios_usuarios

# Register your models here.
admin.site.register(categorias_juegos)
admin.site.register(posteos_usuarios)
admin.site.register(contacta_nos)
admin.site.register(comentarios_usuarios)