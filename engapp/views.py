from string import Template
from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

# Create your views here.
class ListBookView(ListView):
    template_name = "engapp/home.html"
    model = Book