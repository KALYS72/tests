from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


from .views import RegisterAPIView

urlpatterns = [
    path('regisster/', RegisterAPIView.as_view()),
]