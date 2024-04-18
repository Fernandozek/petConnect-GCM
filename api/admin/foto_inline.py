from django.contrib import admin

from ..models import Foto


class FotoInline(admin.StackedInline):
    model = Foto

    extra = 0
