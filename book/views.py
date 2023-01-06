from django.views import generic

from .models import Book


class BookList(generic.ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'


class BookDetail(generic.DetailView):
    model = Book
    template_name = 'book/book_detail.html'


class BookCreatePost(generic.CreateView):
    model = Book
    fields = ['title', 'description', 'author', 'price', ]
    template_name = 'book/create_post.html'
