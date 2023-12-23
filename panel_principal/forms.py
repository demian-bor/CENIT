from django import forms
from .models import contacta_nos, categorias_juegos, posteos_usuarios, comentarios_usuarios

# Formulario de contacto
class form_contacto(forms.ModelForm):
    class Meta:
        model = contacta_nos
        fields = ['contact_name','contact_mail','contact_question']
        labels = {
            'contact_name' : 'Nombre',
            'contact_mail' : 'Correo',
            'contact_question' : 'Consulta'
        }

# Formulario para registrar posteo
class form_posteo(forms.ModelForm):
    class Meta:
        model = posteos_usuarios
        fields = ['post_title','post_subtitle','post_description','post_image','post_category']
        labels = {
            'post_title' : 'Titulo',
            'post_subtitle' : 'Descripcion corta',
            'post_description' : 'Descripcion extendida',
            'post_image' : 'Imagen',
            'post_category' : 'Categoria',
            'post_author' : 'Autor'
        }


# Formulario de registro comentarios
class form_comentario(forms.ModelForm):
    class Meta:
        model = comentarios_usuarios
        fields = ['comment_text']
        labels = {
            'comment_text' : 'Comentario'
        }

# Formulario para registro de categoria
class form_nueva_categoria(forms.ModelForm):
    class Meta:
        model = categorias_juegos
        fields = ['category_name']
        labels = {
            'category_name' : 'Categoria'
        }


