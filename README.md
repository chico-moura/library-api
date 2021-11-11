# library-api
A simple library API. \
It follows a hexagonal achitecture and uses Django REST Framework.\
This is part of a series of challanges.

## Run

Activate enviroment
```
poetry shell
```

Prepare database (if is the first time running)
```
python manage.py makemigrations
python manage.py migrate
```

Run server
```
python manage.py runserver
```

## Routes

List authors (GET):
```
localhost:8000/api/authors
```

Filter books (GET) and create book (POST)
```
localhost:8000/api/books
```

Book details (GET), edit book (POST) and delete book (DELETE)
```
localhost:8000/api/books/<book_id:uuid>
```


## Adding authors from csv file to database:
```
python manage.py import_authors file_name.csv
```
