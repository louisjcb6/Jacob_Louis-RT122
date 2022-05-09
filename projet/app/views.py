
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from app.models import Category, Book

# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = "books.html"
    context_object_name = 'books'


class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    template_name = "book_create.html"
    success_url = '/'


class BookUpdateView(UpdateView):
    model = Book
    template_name = "book_create.html"
    fields = '__all__'
    success_url = '/'


class BookDeleteView(DeleteView):
    model = Book
    template_name = "delete.html"
    success_url = '/'




class CategoryListView(ListView):
    model = Category
    template_name = "category_list.html"
    context_object_name = 'category'


class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    template_name = "category_create.html"
    success_url = '/'


class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = "category_create.html"
    success_url = '/'


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'
    template_name = "category_delete.html"





