from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

# Formulario de registro
class formulario_registro(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['first_name','last_name','username','password1','password2','password1','email','telefono','domicilio']