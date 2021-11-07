from django.urls import path

from api.views.list_authors_view import ListAuthorsView


urlpatterns = [
    path('authors', ListAuthorsView.as_view()),
    # path('books'),
    # path('books/<str:raw_id>')
]
