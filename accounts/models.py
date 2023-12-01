from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Definición de la clase CustomUser que hereda de AbstractBaseUser y PermissionsMixin
class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Definición de campos del modelo
    username = models.CharField(
        _('username'),
        max_length=150,
    )
    email = models.EmailField(
        _('email address'),
        unique=True,
    )
    age = models.PositiveIntegerField(('Age'), default=0, blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    data_joined = models.DateTimeField(_('data joined'), default=timezone.now)

    # Definición de un objeto de gestión de usuarios personalizado
    objects = UserManager()

    # Configuración adicional para el modelo de usuario personalizado
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        # Configuración meta del modelo
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'users'
        swappable = 'AUTH_USER_MODEL'

    def clean(self):
        # Método para normalizar el campo de correo electrónico antes de la validación
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        # Método para enviar un correo electrónico al usuario
        send_mail(subject, message, from_email, [self.email], **kwargs)