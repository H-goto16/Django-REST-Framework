from .models import Info
from .serializers import InfoSerializer
from rest_framework import viewsets

class InfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer