from django.contrib import admin
from appli.models import Articles

@admin.register(Articles)
class AdminRegister(admin.ModelAdmin):
    pass
