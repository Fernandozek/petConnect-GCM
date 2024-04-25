from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Foto
from ..serializers import FotoSerializer


class FotoViewSet(viewsets.ModelViewSet):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]

    search_fields = [
        
    ]
