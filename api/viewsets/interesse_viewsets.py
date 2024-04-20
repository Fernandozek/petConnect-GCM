from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Interesse
from ..serializers import InteresseSerializer


class InteresseViewSet(viewsets.ModelViewSet):
    queryset = Interesse.objects.all()
    serializer_class = InteresseSerializer
    # permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]

    search_fields = [
        
    ]
