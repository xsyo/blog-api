from django.urls import path

from .views import (PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, 
                    СommentListCreateAPI)

app_name = 'blog'

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments', СommentListCreateAPI.as_view(), name='comment-list'),
]