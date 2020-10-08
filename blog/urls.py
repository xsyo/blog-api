from django.urls import path

from .views import (PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, 
                    СommentListCreateAPIView, LikeAPIView, HeadingListAPIView,
                    username_check, email_check)

app_name = 'blog'

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', СommentListCreateAPIView.as_view(), name='comment-list'),
    path('posts/<int:post_id>/like/', LikeAPIView.as_view(), name='like'),
    path('headings/', HeadingListAPIView.as_view(), name='headongs'),
    path('username-check/', username_check, name='username_check'),
    path('email-check/', email_check, name='email_check'),
]