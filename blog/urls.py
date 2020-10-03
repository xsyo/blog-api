from django.urls import path

from .views import PostListCreateAPIView

app_name = 'blog'

urlpatterns = [
    path('posts', PostListCreateAPIView.as_view())
]