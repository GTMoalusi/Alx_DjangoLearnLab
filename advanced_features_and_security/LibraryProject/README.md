#Introduction to Django
Permissions and Groups Setup Guide
This guide explains how custom permissions and groups are configured in the application to control user access.

1. Custom Permissions in models.py
   Custom permissions are defined in the Meta class of the Book model within bookshelf/models.py.

class Meta:
permissions = (
("can_view", "Can view book"),
("can_create", "Can create book"),
("can_edit", "Can edit book"),
("can_delete", "Can delete book"),
)

Django automatically creates these permissions in the database when migrations are run. The full permission string is in the format app_name.permission_name, so these permissions are bookshelf.can_view, bookshelf.can_create, etc.

2. Enforcing Permissions in views.py
   The @permission_required decorator is used to protect views and ensure that only users with the correct permissions can access them. For example:

from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
...

The raise_exception=True argument tells Django to show a 403 Forbidden error page if a user attempts to access the view without the required permission.

3. Django Admin Site Setup
   After running makemigrations and migrate, you must set up the groups in your Django admin site to assign these new permissions.

Step-by-step guide:

Log in to the Django Admin Site: Go to http://127.0.0.1:8000/admin and log in with your superuser credentials.

Create Groups:

In the "Authentication and Authorization" section, click on "Groups".

Click "Add group" in the top right corner.

Create the following groups and assign permissions as specified:

Editors:

Give this group bookshelf.can_create and bookshelf.can_edit permissions.

Viewers:

Give this group only the bookshelf.can_view permission.

Admins:

Give this group all four permissions: bookshelf.can_view, bookshelf.can_create, bookshelf.can_edit, and bookshelf.can_delete.

Assign Users to Groups:

Go back to the main admin page and click on "Users".

Click on a user you want to edit.

In the "Permissions" section, you can add the user to one or more of the groups you created.

Save the user.

4. Testing Permissions
   After assigning users to groups, log in as different users and test the following:

Log in as an 'Editors' user: You should be able to create and edit books, but not delete them.

Log in as a 'Viewers' user: You should only be able to view the list of books. Accessing the create, edit, or delete views should result in a 403 Forbidden error.

Log in as an 'Admins' user: You should have full control and be able to create, view, edit, and delete books.
