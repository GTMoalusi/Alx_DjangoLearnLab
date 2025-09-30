Book API Service
This is a simple Django REST Framework (DRF) application exposing a CRUD (Create, Read, Update, Delete) API for managing books. It implements read-only access for unauthenticated users and full read/write access for authenticated users using the IsAuthenticatedOrReadOnly permission class.

1. Required Configuration
   To run this API, you must have Django and Django REST Framework installed and configured in your project.

1.1. Project Settings (settings.py)

Ensure that rest_framework is added to your INSTALLED_APPS:

INSTALLED_APPS = [
# ... other apps
'rest_framework',
'api', # Assuming your app is named 'api'
]

1.2. Global Permissions (Optional)

While the permissions are set directly on the views (api/views.py), you can define default settings in settings.py if desired (this is not strictly required but often useful):

REST_FRAMEWORK = {
'DEFAULT_PERMISSION_CLASSES': [
'rest_framework.permissions.AllowAny' # Default to open access globally
], # Other settings like authentication classes (e.g., Token or Session Auth)
'DEFAULT_AUTHENTICATION_CLASSES': [
'rest_framework.authentication.SessionAuthentication',
'rest_framework.authentication.TokenAuthentication',
]
}

Note: For write operations to succeed, you must set up an appropriate authentication backend (e.g., Session Authentication for browser access, or Token Authentication for external clients).

2. API Endpoints
   The API provides two main routes for accessing the book resource.

URL Pattern

View Class

HTTP Method

Description

/api/books/

BookListCreateAPIView

GET

List all books.

/api/books/

POST

Create a new book.

/api/books/<pk>/

BookRetrieveUpdateDestroyAPIView

GET

Retrieve details for a specific book.

/api/books/<pk>/

PUT/PATCH

Update a specific book.

/api/books/<pk>/

DELETE

Delete a specific book.

3. Permission Setup: IsAuthenticatedOrReadOnly
   The core of the security model for this API relies on the IsAuthenticatedOrReadOnly permission class, which is applied directly in api/views.py:

api/views.py Snippet

# ...

from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookListCreateAPIView(generics.ListCreateAPIView): # ...
permission_classes = [IsAuthenticatedOrReadOnly]

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): # ...
permission_classes = [IsAuthenticatedOrReadOnly]

Permission Logic Explained

The IsAuthenticatedOrReadOnly class enforces the following rules for all API methods:

Action

HTTP Method

User Status

Result

Read (List/Retrieve)

GET, HEAD, OPTIONS

Authenticated or Unauthenticated

Allowed. Read access is granted to everyone.

Write (Create/Update/Delete)

POST, PUT, PATCH, DELETE

Authenticated

Allowed. The request will be processed.

Write (Create/Update/Delete)

POST, PUT, PATCH, DELETE

Unauthenticated (Anonymous)

Forbidden (403). The user must log in to modify data.

This setup ensures that the API is publicly readable while maintaining data integrity by requiring authentication for any data manipulation.
