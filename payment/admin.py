from django.contrib import admin
from .models import Wallet, PaymentHistory

# Register your models here.


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):

    list_display = ("user", "balance")

    list_filter = ("balance",)

    search_fields = ("user__username",)

    list_per_page = 50


@admin.register(PaymentHistory)
class PaymentHistoryAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "subscription",
        "wallet",
        "amount",
        "status",
        "created_at",
    )

    list_filter = ("status",)

    ordering = ("-created_at",)

    list_per_page = 50

    search_fields = ("user__username",)

    date_hierarchy = "created_at"
