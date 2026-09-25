from django.urls import path
from .views import PaymentRequestAPI

urlpatterns = [
   path('request/',PaymentRequestAPI.as_view(),name='zarinpal-requset'), 
   path('callback/',PaymentRequestAPI.as_view(),name='zarinpal-callback'), 
]