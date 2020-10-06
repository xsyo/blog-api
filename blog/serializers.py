from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Heading, Post, Сomment



class HeadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Heading
        fields = ('id', 'name')


class PostCreateSerializer(serializers.ModelSerializer):
    '''Сериализатор для создания поста'''
    
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'img', 'heading')

    def create(self, validated_data):
        '''Задает автора поста авторизованным пользователем'''
        user = validated_data.pop('user')
        post_author = get_user_model().objects.get(id=user.id)
        new_post = Post.objects.create(author=post_author, **validated_data)
        return new_post


class PostListSerializer(serializers.ModelSerializer):
    '''Сериализатор для списка постов'''

    author = serializers.StringRelatedField()
    heading = serializers.StringRelatedField()
    img_thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Post
        fields = ( 'id', 'title', 'author', 'heading', 'img_thumbnail', 'published', 'likes_count', 'comments_count')


class PostSerializer(serializers.ModelSerializer):
    '''Сериализатор постов'''

    author = serializers.StringRelatedField()
    heading = HeadingSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'heading', 'content', 'img',  'published', 'likes_count', 'comments_count')


class СommentSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField()

    class Meta:
        model = Сomment
        fields = ('id', 'author', 'text', 'created_at')