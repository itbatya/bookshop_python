from django.shortcuts import render, redirect
from .models import Book

def book_page(request):
    book_list = Book.objects.all()
    return render(request, "index.html", {"book_list" : book_list})

def main_page(request):
    return redirect(book_page)

def add_page(request):
    return render(request, "addbook.html")

def add_book(request):
    data = request.POST
    title = data["title"]
    subtitle = data["subtitle"]
    description = data["description"]
    price = data["price"]
    genre = data["genre"]
    author = data["author"]
    year = data["year"]
    book = Book(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    
    book.save()
    
    return redirect(add_page)