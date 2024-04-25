from django.contrib import admin
from .foto_inline import FotoInline

from ..models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'raca',
        'especie',   
        'idade',
        'tamanho',
        'sexo',
        'descricao',
        'personalidade',
        'adotado',
        'created_at',
        'updated_at',
        'user',     
    ]

    search_fields = [
       'id',
        'raca',
        'especie',   
        'idade',
        'tamanho',
        'sexo',
        'descricao',
        'personalidade',
        'adotado',
        'created_at',
        'updated_at',
        'user',   
    ]

    inlines = [FotoInline]
