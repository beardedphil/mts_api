from rest_framework import serializers
from .models import Source


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = ('id', 'url', 'source', 'proper_source')
