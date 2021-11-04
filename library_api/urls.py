from django.contrib import admin
from django.urls import path, include

from api.views.authors_view import AuthorView


authors = [
    path('', AuthorView.as_view()),
    path('create/'),
    path('detail/<str:raw_id>'),
    path('update/<str:raw_id>'),
    path('delete/<str:raw_id>')
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', include(authors)),
]

