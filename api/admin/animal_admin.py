from django.contrib import admin

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
