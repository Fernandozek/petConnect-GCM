from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Animal
from ..serializers import AnimalSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
   

    filter_backends = [filters.SearchFilter]

    search_fields = [
        'raca',        
        'especie',
        
    ]
