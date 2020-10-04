from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404

from .models import Post, Сomment
from .serializers import (PostCreateSerializer, PostListSerializer, 
                            PostSerializer, СommentSerializer)
from .permissions import IsAuthorOrReadOnly


class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()

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


class СommentListCreateAPI(ListCreateAPIView):
    
    serializer_class = СommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return Сomment.objects.filter(post=post)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post__id=self.kwargs['post_id'])

    