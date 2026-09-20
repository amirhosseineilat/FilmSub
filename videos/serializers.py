from rest_framework import serializers
from .models import Video,Comment,Rating,WatchHistory

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user']  

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'  
        read_only_fields = ['user']

class WatchHistorySerializer(serializers.ModelSerializer): 
    class Meta:
        model = WatchHistory
        fields = ['remaining']  
