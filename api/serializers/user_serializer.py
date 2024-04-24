from rest_framework import serializers

from django.contrib.auth.models import User

from ..models.profile import Profile


class UserSerializer(serializers.ModelSerializer):
    tipo_usuario = serializers.SerializerMethodField()
    def get_tipo_usuario(self, obj):
        try:
            profile = Profile.objects.get(user = obj.id)
            return profile.tipo_usuario if profile else None
        except:
            return None
    class Meta:
        model = User
        fields = ["id", "tipo_usuario"]
