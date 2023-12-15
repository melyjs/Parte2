from rest_framework.serializers import ModelSerializer
from .models import Cursos

class CursosSerializer(ModelSerializer):
    class Meta:
        model = Cursos
        fields = "__all__"