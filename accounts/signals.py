from django.contrib.auth import user_logged_in
from django.dispatch import receiver
from .models import LoginHistory

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    # Obtener la IP del cliente
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    # Actualizar contador del usuario
    user.login_count += 1
    user.last_login_ip = ip
    user.save()
    
    # Registrar el historial de inicio de sesión
    LoginHistory.objects.create(
        user=user,
        ip_address=ip
    )