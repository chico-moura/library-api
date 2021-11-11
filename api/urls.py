from django.urls import path

from api.views.books.book_details_view import BookDetailsView
from api.views.books.books_view import BooksView
from api.views.list_authors_view import ListAuthorsView


urlpatterns = [
    path('authors', ListAuthorsView.as_view(), name='authors'),
    path('books', BooksView.as_view(), name='books'),
    path('books/<uuid:book_id>', BookDetailsView.as_view(), name='book_details')
]
