from django.contrib import admin

# Register your models here.
from .models import Cores

class CorAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'cor',
        'slug',
        'criado',
        'modificado',
    ]
    ordering = ['-cor']
    search_fields = ['cor','id']
    list_filter = ['modificado']
    list_editable = ['cor']

admin.site.register(Cores, CorAdmin)