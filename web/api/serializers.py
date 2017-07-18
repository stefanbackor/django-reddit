from rest_framework import serializers
from ..models import Article
from ..models import Reddit

class RedditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reddit
        fields = ['pk', 'name', 'description']

class ArticleSerializer(serializers.ModelSerializer):
    reddit = RedditSerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
