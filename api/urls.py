from django.urls import path

from api.views.list_authors_view import ListAuthorsView


urlpatterns = [
    path('authors', ListAuthorsView.as_view(), name='authors'),
    # path('books'),
    # path('books/<str:raw_id>')
]
