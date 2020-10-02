from rest_framework import serializers

from .models import Heading, Post, Сomment



class HeadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Heading
        fields = ('id', 'name')

class PostListSerializer(serializers.HyperlinkedModelSerializer):
    '''Сериализатор для списков поста'''

    heading = serializers.StringRelatedField()
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ('url', 'title', 'author', 'img', 'heading', 'published', 'likes_count', 'comments_count')
        read_only_fields = ('author', 'heading')
        