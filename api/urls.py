from django.urls import path

from api.views.books.books_view import BooksView
from api.views.list_authors_view import ListAuthorsView


urlpatterns = [
    path('authors', ListAuthorsView.as_view(), name='authors'),
    path('books', BooksView.as_view(), name='books'),
    # path('books/<str:raw_id>')
]
