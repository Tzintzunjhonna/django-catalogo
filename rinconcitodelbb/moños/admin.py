from django.contrib import admin
from .models import Moño

# Register your models here.

class MoñoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Moño, MoñoAdmin)
