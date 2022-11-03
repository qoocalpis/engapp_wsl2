from string import Template
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Book

# Create your views here.
class ListBookView(ListView):
    template_name = "engapp/book_list.html"
    model = Book


class DetailBookView(DetailView):
    template_name = "engapp/book_detail.html"
    model = Book


class CreateBookView(CreateView):
    template_name = "engapp/book_create.html"
    model = Book
    fields = ('title','text','category')
