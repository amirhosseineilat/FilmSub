from django.urls import path
from .views import (
    SubscriptionTypeListCreateAPIView,
    SubscriptionTypeRetrieveUpdateDestroyAPIView,
    SubscriptionCreateAPIView,
    MySubscriptionListAPIView,)

urlpatterns = [
    path('subscription-types/', SubscriptionTypeListCreateAPIView.as_view(), name='subscription-type-list-create'),
    path('subscription-types/<int:pk>/', SubscriptionTypeRetrieveUpdateDestroyAPIView.as_view(), name='subscription-type-retrieve-update-destroy'),
    path('subscriptions/', SubscriptionCreateAPIView.as_view(), name='subscription-create'),
    path('my-subscriptions/', MySubscriptionListAPIView.as_view(), name='my-subscription-list'),
]    
