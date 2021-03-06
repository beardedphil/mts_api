from rest_framework import viewsets
from .models import Source
from .serializers import SourceSerializer


class SourceView(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
