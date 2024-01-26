# bookstore/urls.py
from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDeleteView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<str:isbn>/', BookRetrieveUpdateDeleteView.as_view(), name='book-retrieve-update-delete'),
]

