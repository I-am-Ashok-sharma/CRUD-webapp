from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView ,DetailView,CreateView,UpdateView,DeleteView
from .models import Book
# Create your views here.

class Booklistview(ListView):
    model = Book

class Bookdetailview(DetailView):
    model = Book

class Bookcreateview(CreateView):
    model=Book
    fields =('title','author','price','pages')

class BookUpdateview(UpdateView):
    model=Book
    fields =('title','author','price','pages')


class BookDeleteview(DeleteView):
    model =Book
    success_url = reverse_lazy('Home')
