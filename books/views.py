from django.shortcuts import render, get_object_or_404
from .models import Book

def all_books(request):
    """ A view to return all books """

    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'books/books.html', context)

def book_detail(request, book_id):
    """ A view to return the details of the selected book """

    book = get_object_or_404(Book, pk=book_id)
        
    if book.disc_price:
        points = int(book.disc_price * 100)
    else:
        points = int(book.price * 100)

    context = {
        'book': book,
        'points': points,
    }

    return render(request, 'books/book_detail.html', context)