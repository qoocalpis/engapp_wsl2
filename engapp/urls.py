from django.urls import path
from .views import ListBookView,DetailBookView,CreateBookView

urlpatterns = [
    path("book/",ListBookView.as_view()),
    path("book/<int:pk>/detail",DetailBookView.as_view()),
    path('book/create/',CreateBookView.as_view()),
]