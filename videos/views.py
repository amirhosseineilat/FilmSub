from django.shortcuts import get_object_or_404, render
from rest_framework import status
from .models import Video,Comment,Rating,WatchHistory
from .serializers import VideoSerializer,CommentSerializer,RatingSerializer,WatchHistorySerializer
from rest_framework.views import APIView, Response 
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.

class VideoListCreateAPIView(ListCreateAPIView):

    serializer_class = VideoSerializer

    def get_queryset(self):
        return Video.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]

        elif self.request.method == 'POST':
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

class VideoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
            return Video.objects.all()
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]

        elif self.request.method in ['PATCH','PUT']:
            permission_classes = [IsAuthenticated]

        elif self.request.method == 'DELETE':
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

class CommentListCreateAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]

        elif self.request.method == 'POST':
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]

        elif self.request.method in ['PATCH','PUT']:
            permission_classes = [IsAuthenticated]

        elif self.request.method == 'DELETE':
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class RatingListCreateAPIView(ListCreateAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]

        elif self.request.method == 'POST':
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RatingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]

        elif self.request.method in ['PATCH','PUT']:
            permission_classes = [IsAuthenticated]

        elif self.request.method == 'DELETE':
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]
    def perform_update(self, serializer):   
        serializer.save(user=self.request.user)

class WatchHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        watch_history = WatchHistory.objects.filter(user=request.user)
        serializer = WatchHistorySerializer(watch_history, many=True)
        return Response(serializer.data)

    def post(self, request,video_id):
        video = get_object_or_404(Video, id=video_id)

        serializer = WatchHistorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        history, created = WatchHistory.objects.update_or_create(user=request.user, video=video,defaults={'remaining': serializer.validated_data['remaining']}) 

        return Response(WatchHistorySerializer(history).data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)