from rest_framework import viewsets
from .serializers import ArticleSerializer
from .serializers import RedditSerializer
from ..models import Article
from ..models import Reddit

class RedditViewSet(viewsets.ModelViewSet):
    model = Reddit
    serializer_class = RedditSerializer
    queryset = Reddit.objects.all()

class ArticleViewSet(viewsets.ModelViewSet):
    model = Article
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
