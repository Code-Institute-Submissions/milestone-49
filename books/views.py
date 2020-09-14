from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Book, Category

def all_books(request):
    """ A view to return all books """

    books = Book.objects.all()
    query = None
    category = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            books = books.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a keyword or ISBN to search.")
                return redirect(reverse('books'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(description_full__icontains=query) | Q(isbn10__icontains=query) | Q(isbn13__icontains=query) | Q(category__friendly_name__icontains=query) 

            books = books.filter(queries)

    context = {
        'books': books,
        'search_term': query,
        'current_categories': categories,
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