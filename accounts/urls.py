from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Importa las vistas definidas en tu aplicación

# Configuración de las URL para la aplicación de autenticación

urlpatterns = [
    # URL para el registro de usuarios
    path('signup/', views.UserCreateAndLoginView.as_view(), name='signup'),

    # URL para la vista de inicio de sesión
    path('login/', LoginView.as_view(
        redirect_authenticated_user=True,  # Redirigir usuarios autenticados a otra página
        template_name='accounts/login.html'  # Usar una plantilla personalizada para el inicio de sesión
    ), name='login'),

    # URL para la vista de cierre de sesión
    path('logout/', LogoutView.as_view(), name='logout'),

    # URL para ver detalles del usuario
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDone.as_view(),name='password_change_done'),
    path('user_delete/<int:pk>/', views.UserDelete.as_view(), name='user_delete'),
]