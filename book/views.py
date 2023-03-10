from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .models import Book
from .forms import CommentForm


class BookList(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'book/book_list.html'
    context_object_name = 'books'


# class BookDetail(generic.DetailView):
#     model = Book
#     template_name = 'book/book_detail.html'


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_comments = book.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()

    else:
        comment_form = CommentForm()
    return render(request, 'book/book_detail.html', {
        'book': book,
        'comments': book_comments,
        'comment_form': comment_form,
    })


class BookCreatePost(LoginRequiredMixin, generic.CreateView):
    model = Book
    fields = ['title', 'description', 'author', 'price', 'cover', ]
    template_name = 'book/create_post.html'


class BookUpdatePost(LoginRequiredMixin, UserPassesTestMixin,generic.UpdateView):
    model = Book
    fields = ['title', 'description', 'author', 'cover', ]
    template_name = 'book/update_post.html'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class BookDeletePost(LoginRequiredMixin, UserPassesTestMixin ,generic.DeleteView):
    model = Book
    template_name = 'book/delete_post.html'
    success_url = reverse_lazy('book_list')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user