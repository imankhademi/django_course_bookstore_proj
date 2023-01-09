from django.views import generic
from django.urls import reverse_lazy

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
    fields = ['title', 'description', 'author', 'price', 'cover', ]
    template_name = 'book/create_post.html'


class BookUpdatePost(generic.UpdateView):
    model = Book
    fields = ['title', 'description', 'author', 'cover', ]
    template_name = 'book/update_post.html'


class BookDeletePost(generic.DeleteView):
    model = Book
    template_name = 'book/delete_post.html'
    success_url = reverse_lazy('book_list')
