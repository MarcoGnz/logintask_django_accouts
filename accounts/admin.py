from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

# Definición de una clase UserAdmin que extiende de BaseUserAdmin proporcionado por Django
class UserAdmin(BaseUserAdmin):
    # Especifica los campos que se mostrarán en la lista de usuarios en el panel de administración
    list_display = (
        "username",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
    )

    # Define los campos que se mostrarán al agregar un nuevo usuario en el panel de administración
    add_fieldsets = (
        (None, {
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
            )}
         ),
    )
    
    # Define los campos que se mostrarán al ver o editar un usuario existente en el panel de administración
    fieldsets = (
        (None, {'fields': (
            'username',
            'email',
            'age',  # Se agrega 'age' como campo adicional en este ejemplo
            'password'
        )}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions'
        )}),
    )

    # Define los campos que se pueden utilizar para buscar usuarios en el panel de administración
    search_fields = ('username', 'email') 

# Registra la clase UserAdmin para el modelo CustomUser en el panel de administración
admin.site.register(CustomUser, UserAdmin)