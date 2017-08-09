from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ArticleSerializer
from .serializers import RedditSerializer
from ..models import Article
from ..models import Reddit


class RedditViewSet(viewsets.ModelViewSet):
    """
    *Ahoj*
    """
    model = Reddit
    serializer_class = RedditSerializer
    queryset = Reddit.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class ArticleViewSet(viewsets.ModelViewSet):
    model = Article
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('reddit',)
