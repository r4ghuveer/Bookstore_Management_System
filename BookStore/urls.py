# BookStore/urls.py

from django.contrib import admin
from django.urls import path, include
from bookstore_app.views import BookListCreateView, BookRetrieveUpdateDeleteView, home
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',include('bookstore_app.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/books/', BookListCreateView.as_view(), name='book-list-create'),
    path('api/books/<str:isbn>/', BookRetrieveUpdateDeleteView.as_view(), name='book-detail'),
    path('api/token/', obtain_auth_token, name='token_obtain_pair')
]

