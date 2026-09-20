from django.urls import path
from .views import (
    VideoListCreateAPIView,
    VideoRetrieveUpdateDestroyAPIView,
    CommentListCreateAPIView,
    CommentRetrieveUpdateDestroyAPIView,
    RatingListCreateAPIView,
    RatingRetrieveUpdateDestroyAPIView,
    WatchHistoryAPIView,
)   

urlpatterns = [
    path('videos/', VideoListCreateAPIView.as_view(), name='video-list-create'),
    path('videos/<int:pk>/', VideoRetrieveUpdateDestroyAPIView.as_view(), name='video-retrieve-update-destroy'),
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-retrieve-update-destroy'),
    path('ratings/', RatingListCreateAPIView.as_view(), name='rating-list-create'),
    path('ratings/<int:pk>/', RatingRetrieveUpdateDestroyAPIView.as_view(), name='rating-retrieve-update-destroy'),
    path('watch-history/<int:video_id>/', WatchHistoryAPIView.as_view(), name='watch-history-list-create'),
]