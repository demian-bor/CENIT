from django.db import models


# Modelo para la tabla de contacto
class contacta_nos(models.Model):
    contact_ticket = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=100, null=False,default="Ingresa tu nombre")
    contact_mail = models.CharField(max_length=100, null=False,default="Ingresa tu correo")
    contact_question = models.TextField(null=False,default="Ingresa tu consulta")


# Modelo para la lista de categorias
class categorias_juegos(models.Model):
    categorias_predefinidas = (
        ('shooter','Shooters'),
        ('rpg','RPG'),
        ('sports','Deportes'),
        ('action','Accion'),
        ('simulation','Simulacion'),
        ('VR','Realidad Virtual'),
        ('arcade','Arcades')
    )
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(choices=categorias_predefinidas,max_length=50)

    def __str__(self):
        return self.category_name


# Modelo para el posteo de usuarios
class posteos_usuarios(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_author = models.CharField(max_length=50, null=False)
    post_title = models.CharField(max_length=50, null=False,default="Titulo del articulo")
    post_subtitle = models.CharField(max_length=100, null=False,default="Descripcion corta del articulo")
    post_description = models.TextField(null=False,default="Ingresa la descripcion larga del articulo")
    post_image = models.ImageField(null=True, blank=True, upload_to='post-images')
    post_category = models.ForeignKey(categorias_juegos, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    post_active = models.BooleanField(default=True)

    class Meta:
            ordering = ('-post_date',)

    def __str__(self):
        return self.post_title

    def delete(self, using = None, keep_parents = False):
        self.post_image.delete(self.post_image.name)
        super().delete()


# Modelo para la lista de comentarios
class comentarios_usuarios(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_author = models.CharField(max_length=50, null=False)
    comment_text = models.TextField(null=False,default="Ingresa tu comentario")
    comment_related_post = models.ForeignKey(posteos_usuarios, on_delete=models.SET_NULL, null=True, default='Sin comentarios')
    comment_date = models.DateTimeField(auto_now_add=True)





