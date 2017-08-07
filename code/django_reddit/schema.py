from graphene_django import DjangoObjectType
from graphene_django.debug import DjangoDebug
import graphene

from web.graphql.schema import Query as web_Query


class Query(web_Query,
            graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query)
