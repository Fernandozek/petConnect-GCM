from django.contrib import admin

from ..models import Foto


@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = [
        'id',        
        'animal',
    ]

    search_fields = [
        'id',        
        'animal',
    ]


