from django.urls import path 
from .views import Register,UserActive
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path("register/",Register.as_view()),
    path("login/",TokenObtainPairView.as_view()),
    path("token/refresh/",TokenRefreshView.as_view()),
    path("me/",UserActive.as_view()),
]