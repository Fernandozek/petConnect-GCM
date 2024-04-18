from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AnimalViewSet


# Cria um roteador padrão
router = DefaultRouter()
# Registra o viewset do Animal com o roteador
router.register(r'animais', AnimalViewSet)

urlpatterns = [
    # Inclui as URLs geradas pelo roteador
    path('', include(router.urls)),
    # Adicione outras URLs aqui, se necessário
]