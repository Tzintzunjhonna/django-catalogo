from django.contrib import admin
from .models import Biberon

# Register your models here.

class BiberonAdmin(admin.ModelAdmin):
    reandoly_fields = ('created', 'update')

admin.site.register(Biberon, BiberonAdmin)