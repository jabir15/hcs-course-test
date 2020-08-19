from django.contrib import admin
from .models import Standard, Subject, Chapter, Topic, LoginLogoutLog
# Register your models here.

admin.site.register(Standard)
admin.site.register(Subject)
admin.site.register(Chapter)
admin.site.register(Topic)
admin.site.register(LoginLogoutLog)
