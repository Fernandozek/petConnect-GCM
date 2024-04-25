from django.contrib import admin

from ..models import Interesse


@admin.register(Interesse)
class InteresseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'animal',
    ]

    search_fields = [
        'id',
        'user',
        'animal',
    ]

 
