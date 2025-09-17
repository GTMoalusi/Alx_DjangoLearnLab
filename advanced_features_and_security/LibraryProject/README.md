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

#=================================================================================#
Implemented Security Measures
This document outlines the security enhancements made to the Django application, following the best practices for preventing common web vulnerabilities.

1. Secure Settings (settings.py)
   DEBUG = False: Ensures that sensitive debugging information is not exposed to the public in a production environment.

CSRF_COOKIE_SECURE = True: Forces the csrftoken cookie to be sent over HTTPS only, protecting against man-in-the-middle attacks.

SESSION_COOKIE_SECURE = True: Forces the session cookie to be sent over HTTPS only, similarly protecting user sessions.

SECURE_CONTENT_TYPE_NOSNIFF = True: Adds the X-Content-Type-Options: nosniff header, preventing browsers from incorrectly interpreting file types and mitigating XSS attacks.

SECURE_BROWSER_XSS_FILTER = True: Adds the X-XSS-Protection header for older browsers.

X_FRAME_OPTIONS = 'DENY': Prevents the site from being loaded in a frame, protecting against clickjacking attacks.

2. CSRF Protection (Templates)
   All forms that accept user input are now required to include the {% csrf_token %} template tag. This automatically inserts a hidden input field with a unique, user-specific token. Django's middleware verifies this token on form submission, rejecting any requests that do not have a valid token. This protects against Cross-Site Request Forgery (CSRF).

3. Secure Data Access (views.py)
   ORM Usage: Direct SQL queries or string formatting for user-provided input have been replaced with the Django ORM. The ORM's methods, such as filter(), automatically handle the parameterization of queries, which makes them immune to SQL injection attacks.

Input Handling: The search functionality in bookshelf/views.py now uses a safe, Q-object-based query to filter results, ensuring user input does not directly affect the database query structure.

Custom CSRF Failure View: A custom view is now available to provide a more user-friendly error page if a CSRF attack is detected, rather than showing a generic server error.

4. Content Security Policy (CSP)
   The django-csp middleware has been configured to add a Content-Security-Policy header to all responses. This policy restricts where the browser can load content (scripts, styles, etc.) from, preventing many types of XSS attacks.
