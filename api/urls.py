from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AnimalViewSet, FotoViewSet, UserViewSet, InteresseViewSet, ProfileViewSet
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from rest_framework_simplejwt import views as jwt_views


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
    path('login/', obtain_jwt_token, name='login_jwt'),
    path('atualizar_token/', refresh_jwt_token, name='atualizar_jwt'),
    path('verificar_token/', verify_jwt_token, name='verificar_jwt'),   
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/', include('djoser.urls')),
]