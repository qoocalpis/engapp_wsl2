from django.urls import path
from .views import ListBookView

urlpatterns = [
    path("",ListBookView.as_view(),name="home"),
]