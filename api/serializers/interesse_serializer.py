from rest_framework import serializers

from ..models import Interesse


class InteresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interesse
        fields = '__all__'
