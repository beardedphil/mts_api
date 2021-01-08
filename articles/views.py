from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        sources = self.request.query_params.get('sources', None)
        keywords = self.request.query_params.get('keywords', None)

        if sources is not None:
            sources = sources.split()
            for i in range(len(sources)):
                sources[i] = sources[i].lower()

        if keywords is not None:
            keywords = keywords.split()
            for i in range(len(keywords)):
                keywords[i] = keywords[i].lower()

        if sources is not None and keywords is not None:
            queryset = Article.objects.filter(source__in=sources).filter(keywords__contains=keywords)
        elif sources is not None:
            queryset = Article.objects.filter(source__in=sources)
        elif keywords is not None:
            queryset = Article.objects.filter(keywords__contains=keywords)
        else:
            queryset = Article.objects.all()

        return queryset.order_by('-pub_date', 'title', 'id')

