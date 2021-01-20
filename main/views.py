from django.shortcuts import render
from .models import Book

def book_page(request):
    book_list = Book.objects.all()
    return render(request, "index.html", {"book_list" : book_list})
