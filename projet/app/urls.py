from django.urls import path
from app import views


urlpatterns = [
    path('', views.BookListView.as_view(), name='home'),
    path('create-book', views.BookCreateView.as_view(), name='book_create'),
    path('update-book/<int:pk>/', views.BookUpdateView.as_view(), name='book_update'),
    path('delete-book/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete'),
    path('create-category', views.CategoryCreateView.as_view(), name='category_create'),
    path('category', views.CategoryListView.as_view(), name='category'),
    path('update-category/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('delete-category/<int:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),
]
