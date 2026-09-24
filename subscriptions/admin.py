from django.contrib import admin
from .models import SubscriptionType, Subscription

# Register your models here.


@admin.register(Subscription)
class SubscriptionTypeAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "subscription_type",
        "start_time",
        "end_time",
        "status",
    )

    list_filter = (
        "start_time",
        "end_time",
        "status",
    )

    search_fields = (
        "user__username",
        "user__email",
    )

    list_per_page = 50


@admin.register(SubscriptionType)
class SubscriptionTypeAdmin(admin.ModelAdmin):

    list_display = (
        "type",
        "price",
        "duration",
    )

    search_fields = (
        "type",
        "price",
        "duration",
    )

    list_filter = ("type",)

    list_per_page = 50
