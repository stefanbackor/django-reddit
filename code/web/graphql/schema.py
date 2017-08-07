from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import graphene

from ..models import Article
from ..models import Comment
from ..models import Reddit


class RedditType(DjangoObjectType):
    class Meta:
        model = Reddit


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article


class Query(graphene.AbstractType):
    reddit = graphene.Node.Field(RedditType,
                                 id=graphene.Int())
    all_reddits = graphene.List(RedditType)

    article = graphene.Node.Field(ArticleType,
                                  id=graphene.Int(),
                                  reddit=graphene.Int())
    all_articles = graphene.List(ArticleType,
                                 reddit=graphene.Int())

    @graphene.resolve_only_args
    def resolve_reddit(self, args):
        id = args.get('id')
        if id is not None:
            return Reddit.objects.get(pk=id)
        return None

    @graphene.resolve_only_args
    def resolve_article(self, args):
        id = args.get('id')
        if id is not None:
            return Article.objects.get(pk=id)
        return None

    @graphene.resolve_only_args
    def resolve_all_reddits(self):
        return Reddit.objects.all()

    @graphene.resolve_only_args
    def resolve_all_articles(self, reddit=None):
        if reddit:
            return Article.objects.filter(reddit=reddit).all()
        return Article.objects.all()
