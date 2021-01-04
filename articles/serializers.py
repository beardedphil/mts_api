from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'url', 'title', 'source', 'article_link', 'image_link', 'pub_date', 'keywords')
