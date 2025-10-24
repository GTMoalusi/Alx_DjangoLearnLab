Social Media API Backend

This is the backend for a simple social media platform, built using Django and Django Rest Framework (DRF).

This documentation covers the setup process, database migrations, and a guide for testing the core User Accounts and Authentication endpoints.

🚀 Setup and Installation

Follow these steps to get the project running locally.

Prerequisites

Python (3.8+)

pip (Python package installer)

1. Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies.

# Create the virtual environment

python3 -m venv venv

# Activate the virtual environment (Linux/macOS)

source venv/bin/activate

# Activate the virtual environment (Windows)

.\venv\Scripts\activate

2. Install Dependencies

Install all necessary packages, including Django, DRF, and any other required libraries.

pip install django djangorestframework django-filter

3. Database Migrations

Apply the database migrations to create the necessary tables, including the custom User model and the Follow model from the accounts app.

# Create the migration files (if any changes were made or for new apps)

python manage.py makemigrations accounts

# Apply all pending migrations to the database

python manage.py migrate

4. Run the Server

Start the Django development server. The API will be available at http://127.0.0.1:8000/.

python manage.py runserver

🧪 Testing the Endpoints (API v1)

All public endpoints are prefixed with /api/v1/. We will use cURL examples, which can be easily adapted for Postman or similar tools.

🔑 Authentication Endpoints

Endpoint

Method

Description

Requires Auth

/api/v1/accounts/auth/register/

POST

Create a new user account.

No

/api/v1/accounts/auth/login/

POST

Log in and receive an auth token.

No

1. Registration (POST /api/v1/accounts/auth/register/)

Create a new user. The response will include the user data and the token.

curl -X POST [http://127.0.0.1:8000/api/v1/accounts/auth/register/](http://127.0.0.1:8000/api/v1/accounts/auth/register/) \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "email": "user@example.com", "password": "StrongPassword123"}'

2. Login (POST /api/v1/accounts/auth/login/)

Log in with credentials to retrieve the token. This token is required for all protected endpoints.

curl -X POST [http://127.0.0.1:8000/api/v1/accounts/auth/login/](http://127.0.0.1:8000/api/v1/accounts/auth/login/) \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "StrongPassword123"}'

Note: Save the token from the response (e.g., Token ABCDEF123456...).

👤 Profile and Following Endpoints

Endpoint

Method

Description

Requires Auth

/api/v1/accounts/profile/

GET/PUT/PATCH

View/Edit the authenticated user's profile.

Yes

/api/v1/accounts/{username}/

GET

View a public profile by username.

No

/api/v1/accounts/{username}/follow/

POST/DELETE

Follow or Unfollow a user.

Yes

Pre-requisite: For the following examples, assume you have registered a second user, testuser2, and have the token for testuser (saved as $TOKEN).

3. View/Edit Own Profile (GET /api/v1/accounts/profile/)

Retrieve the detailed profile of the authenticated user (testuser).

curl -X GET [http://127.0.0.1:8000/api/v1/accounts/profile/](http://127.0.0.1:8000/api/v1/accounts/profile/) \
-H "Authorization: Token $TOKEN"

Update the profile (e.g., add a bio).

curl -X PATCH [http://127.0.0.1:8000/api/v1/accounts/profile/](http://127.0.0.1:8000/api/v1/accounts/profile/) \
-H "Content-Type: application/json" \
-H "Authorization: Token $TOKEN" \
-d '{"bio": "A passionate API developer.", "full_name": "Test User"}'

4. View Public Profile (GET /api/v1/accounts/testuser2/)

Retrieve the public profile of another user (testuser2). Authentication is optional here.

curl -X GET [http://127.0.0.1:8000/api/v1/accounts/testuser2/](http://127.0.0.1:8000/api/v1/accounts/testuser2/)

5. Follow a User (POST /api/v1/accounts/testuser2/follow/)

The authenticated user (testuser) follows another user (testuser2).

curl -X POST [http://127.0.0.1:8000/api/v1/accounts/testuser2/follow/](http://127.0.0.1:8000/api/v1/accounts/testuser2/follow/) \
-H "Authorization: Token $TOKEN"

# Expected response: {"detail": "Successfully followed testuser2."}

6. Unfollow a User (DELETE /api/v1/accounts/testuser2/follow/)

The authenticated user (testuser) unfollows the user (testuser2).

curl -X DELETE [http://127.0.0.1:8000/api/v1/accounts/testuser2/follow/](http://127.0.0.1:8000/api/v1/accounts/testuser2/follow/) \
-H "Authorization: Token $TOKEN"

# Expected response: {"detail": "Successfully unfollowed testuser2."}
