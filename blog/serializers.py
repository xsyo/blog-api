from rest_framework import serializers

from .models import Heading, Post, Сomment



class HeadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Heading
        fields = ('id', 'name')

class PostListSerializer(serializers.HyperlinkedModelSerializer):
    '''Сериализатор для списков поста'''

    class Meta:
        model = Post
        fields = ('url', 'title', 'author', 'img', 'heading', 'published', 'likes_count', 'comments_count')
        
