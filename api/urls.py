from django.urls import path
from .views import Book
from .views import BookAPIView

urlpatterns = [
    path('', BookAPIView.as_view())
]
