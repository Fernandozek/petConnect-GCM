from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AnimalViewSet, FotoViewSet, UserViewSet, InteresseViewSet, ProfileViewSet


# Cria um roteador padrão
router = DefaultRouter()
# Registra o viewset do Animal com o roteador
router.register(r'animais', AnimalViewSet)
# Registra o viewset do Foto com o roteador
router.register(r'fotos', FotoViewSet)
# Registra o viewset do User com o roteador
router.register(r'users', UserViewSet)
# Registra o viewset do Interesse com o roteador
router.register(r'interesses', InteresseViewSet)
# Registra o viewset do Profile com o roteador
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    # Inclui as URLs geradas pelo roteador
    path('', include(router.urls)),   
    path('auth/', include('djoser.urls')),
]