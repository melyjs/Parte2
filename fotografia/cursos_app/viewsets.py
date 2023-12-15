from rest_framework.viewsets import ModelViewSet
from .models import Cursos
from .serializers import CursosSerializer

class CursosViewSet(ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer