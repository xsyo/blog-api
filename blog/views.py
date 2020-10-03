from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Post
from .serializers import PostCreateSerializer, PostListSerializer, PostSerializer
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




    