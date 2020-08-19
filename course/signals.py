from datetime import datetime,timedelta
from django.utils import timezone
from .models import LoginLogoutLog
import csv

from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver


@receiver(user_logged_in)
def log_user_logged_in(sender, user, request, **kwargs):
    if user.username !='admin':
        user, created = LoginLogoutLog.objects.get_or_create(
            user__username=user,
            defaults = {'user':user, 'total_online_time':timedelta()}
        )
        user.last_login_time = timezone.now()
        user.save(update_fields=['last_login_time'])

@receiver(user_logged_out)
def log_user_logged_out(sender, user, request, **kwargs):
    if user.username !='admin':
        user = LoginLogoutLog.objects.get(user__username=user)
        user.last_logout_time = timezone.now()
        user.total_online_time += user.last_logout_time - user.last_login_time
        user.save()
    

