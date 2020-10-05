from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Post, Сomment, Heading
from .serializers import (PostCreateSerializer, PostListSerializer, 
                            PostSerializer, СommentSerializer, HeadingSerializer)
from .permissions import IsAuthorOrReadOnly



class PostListCreateAPIView(ListCreateAPIView):

    queryset = Post.objects.all()
    filter_fields = ['heading', 'author', 'published']
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCreateSerializer
        else:
            return PostListSerializer


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class СommentListCreateAPIView(ListCreateAPIView):
    
    serializer_class = СommentSerializer

    def get_queryset(self):
        post = self.get_post()
        return Сomment.objects.filter(post=post)


    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


    def get_post(self):
        '''Возвдащяет пост по id взятого из url'''
        return get_object_or_404(Post, id=self.kwargs['post_id'])


class LikeAPIView(APIView):
    '''Добавляет или удаляет лайк пользователя с поста'''

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        if post in request.user.liked_posts.all():
            request.user.liked_posts.remove(post)
            return Response({'event': 'remove'})

        else:
            request.user.liked_posts.add(post)
            return Response({'event': 'add'})


class HeadingListAPIView(ListAPIView):

    queryset = Heading.objects.all()
    serializer_class = HeadingSerializer