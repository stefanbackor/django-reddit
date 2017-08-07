from rest_framework import serializers
from ..models import Article
from ..models import Reddit


class RedditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reddit
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    reddit_id = serializers.PrimaryKeyRelatedField(
        queryset=Reddit.objects.all(), write_only=True, source='reddit')
    reddit = RedditSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
