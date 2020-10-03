from rest_framework.generics import ListCreateAPIView

from .models import Post
from .serializers import PostCreateSerializer, PostListSerialiver


class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCreateSerializer
        else:
            return PostListSerialiver


    