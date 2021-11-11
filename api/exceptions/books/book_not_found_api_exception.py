from rest_framework.exceptions import APIException


class BookNotFoundAPIException(APIException):
    status_code = 404
    default_detail = 'Book not found for given id'
    defualt_code = 'book_not_found'
