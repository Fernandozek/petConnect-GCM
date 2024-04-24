from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.contrib.auth.models import User
from ..serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    filter_backends = [filters.SearchFilter]

    search_fields = [
        
    ]

    @action(methods=['get'], detail=False)
    def me(self, request):
        parametros = self.request.query_params
        return Response(UserSerializer(request.user).data, status=status.HTTP_201_CREATED)