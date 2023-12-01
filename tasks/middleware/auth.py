from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

# Definición de un middleware para la autenticación de usuarios
class AuthMiddleware(MiddlewareMixin):
    # Método que se ejecuta después de procesar una respuesta
    def process_response(self, request, response):
        # Verifica si el usuario no está autenticado y no está en las rutas de inicio de sesión o registro
        if not request.user.is_authenticated and request.path != '/accounts/login/' and request.path != '/accounts/signup/':
            # Redirige al usuario a la página de inicio de sesión
            return HttpResponseRedirect('/accounts/login/')
        # Devuelve la respuesta original si no se cumple la condición
        return response