from django.contrib import admin
from .models import Video, Comment, Rating, WatchHistory

# Register your models here.


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "description",
        "created_at",
        "duration",
        "subscription_type",
        "view_count",
    )

    list_filter = (
        "created_at",
        "subscription_type",
    )

    search_fields = ("title",)

    ordering = "-created_at"

    list_per_page = 50

    date_hierarchy = "created_at"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        "content",
        "user",
        "video",
        "created_at",
    )

    list_per_page = 50

    ordering = "-created_at"

    search_fields = "user__username"

    date_hierarchy = "created_at"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):

    list_display = (
        "score",
        "user",
        "video",
        "created_at",
    )

    list_filter = "score"

    list_per_page = 50

    search_fields = "user__username"

    ordering = "-created_at"


@admin.register(WatchHistory)
class WatchHistoryAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "video",
        "remaining",
        "watched_at",
    )

    list_filter = ("watched_at",)

    list_per_page = 50

    search_fields = "user__username"
