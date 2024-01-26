# bookstore/urls.py
from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDeleteView
from . import views

urlpatterns = [
        path('',views.home),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<str:isbn>/', BookRetrieveUpdateDeleteView.as_view(), name='book-retrieve-update-delete'),
]

