from rest_framework.generics import ListCreateAPIView

from .models import Post
from .serializers import PostListSerializer


class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer