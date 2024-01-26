# bookstore/views.py
from django.http import HttpResponse
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


def home(request):
    return HttpResponse('<h1> Home </h1>')

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'isbn'
