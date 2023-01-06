from django.views import generic

from .models import Book


class BookList(generic.ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'
