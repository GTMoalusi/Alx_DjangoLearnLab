import json
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book

# URLs for API Endpoints
LIST_CREATE_URL = reverse('book-list-create')
# The detail URL requires a primary key (pk) to be formatted
DETAIL_URL = lambda pk: reverse('book-detail', kwargs={'pk': pk})

class BookApiTests(APITestCase):
    """
    Comprehensive unit tests for the Book API endpoints (CRUD, Permissions, and Querying).
    """

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        
        # 1. Users
        cls.user = User.objects.create_user(username='testuser', password='password123')
        cls.admin_user = User.objects.create_superuser(username='admin', password='password123', email='a@a.com')

        # 2. Books
        cls.book1 = Book.objects.create(title='The Fellowship of the Ring', author='J.R.R. Tolkien', publication_year=1954)
        cls.book2 = Book.objects.create(title='The Two Towers', author='J.R.R. Tolkien', publication_year=1954)
        cls.book3 = Book.objects.create(title='Dune', author='Frank Herbert', publication_year=1965)
        cls.book4 = Book.objects.create(title='Foundation', author='Isaac Asimov', publication_year=1951)

    def setUp(self):
        """Standard setup for each test method (clean login state)."""
        self.client.logout()
        
    # --- Helper Functions ---
    def authenticate_user(self, username='testuser', password='password123'):
        """Helper to log in a user for authenticated tests."""
        self.client.login(username=username, password=password)

    # =========================================================================
    # 1. LIST VIEW (GET /api/books/) - Permissions & Basic Listing
    # =========================================================================
    
    def test_list_view_allows_anonymous_read(self):
        """Test that unauthenticated users can view the list of books."""
        response = self.client.get(LIST_CREATE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that all four books are returned
        self.assertEqual(len(response.data), 4)
        self.assertIn('The Fellowship of the Ring', str(response.data))

    def test_list_view_allows_authenticated_read(self):
        """Test that authenticated users can view the list of books."""
        self.authenticate_user()
        response = self.client.get(LIST_CREATE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    # =========================================================================
    # 2. ADVANCED QUERY TESTS (Filtering, Searching, Ordering)
    # =========================================================================

    def test_list_view_filtering_by_title(self):
        """Test filtering the book list by title using a query parameter."""
        # Query for book3 (Dune)
        response = self.client.get(LIST_CREATE_URL, {'title': 'Dune'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Dune')

    def test_list_view_searching_by_author(self):
        """Test searching for books by a partial author name."""
        # Search for 'Tolkien' (should return book1 and book2)
        response = self.client.get(LIST_CREATE_URL, {'search': 'Tolkien'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        
        titles = [book['title'] for book in response.data]
        self.assertIn('The Fellowship of the Ring', titles)
        self.assertIn('The Two Towers', titles)

    def test_list_view_ordering_ascending(self):
        """Test ordering by publication_year in ascending order."""
        # Expected order: Foundation (1951), Fellowship/Towers (1954), Dune (1965)
        response = self.client.get(LIST_CREATE_URL, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Foundation')
        self.assertEqual(response.data[-1]['title'], 'Dune') # Dune is the last one since it's the latest

    def test_list_view_ordering_descending(self):
        """Test ordering by publication_year in descending order."""
        # Expected order: Dune (1965), Fellowship/Towers (1954), Foundation (1951)
        response = self.client.get(LIST_CREATE_URL, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Dune')
        self.assertEqual(response.data[-1]['title'], 'Foundation')

    # =========================================================================
    # 3. CREATE VIEW (POST /api/books/) - Permissions & Creation
    # =========================================================================

    def test_create_view_requires_authentication(self):
        """Test that anonymous users cannot create a book."""
        data = {'title': 'New Book', 'author': 'Anon', 'publication_year': 2024}
        response = self.client.post(LIST_CREATE_URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 4)

    def test_create_view_succeeds_with_authentication(self):
        """Test that authenticated users can successfully create a book."""
        self.authenticate_user()
        data = {
            'title': 'The Martian', 
            'author': 'Andy Weir', 
            'publication_year': 2011
        }
        response = self.client.post(LIST_CREATE_URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 5)
        self.assertEqual(response.data['title'], 'The Martian')
        
        # Verify the book exists in the database
        new_book = Book.objects.get(title='The Martian')
        self.assertEqual(new_book.author, 'Andy Weir')


    # =========================================================================
    # 4. DETAIL VIEW (GET /api/books/<pk>/) - Permissions & Retrieval
    # =========================================================================

    def test_detail_view_allows_anonymous_read(self):
        """Test that unauthenticated users can retrieve a single book."""
        response = self.client.get(DETAIL_URL(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'The Fellowship of the Ring')

    def test_detail_view_returns_404_for_invalid_id(self):
        """Test that an invalid ID returns a 404 Not Found."""
        response = self.client.get(DETAIL_URL(99999))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # =========================================================================
    # 5. UPDATE VIEW (PUT/PATCH /api/books/<pk>/) - Permissions & Updates
    # =========================================================================

    def test_update_view_requires_authentication(self):
        """Test that anonymous users cannot update a book."""
        original_title = self.book3.title
        data = {'title': 'Updated Title by Anon', 'author': 'Frank Herbert', 'publication_year': 1965}
        response = self.client.put(DETAIL_URL(self.book3.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # Verify the title was NOT changed in the database
        self.assertEqual(Book.objects.get(id=self.book3.id).title, original_title)

    def test_update_view_succeeds_with_authentication(self):
        """Test that authenticated users can successfully update a book (PUT)."""
        self.authenticate_user()
        new_data = {
            'title': 'Dune Messiah', 
            'author': 'Frank Herbert', 
            'publication_year': 1969
        }
        response = self.client.put(DETAIL_URL(self.book3.id), new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify the change in the response and database
        self.assertEqual(response.data['title'], 'Dune Messiah')
        self.assertEqual(Book.objects.get(id=self.book3.id).title, 'Dune Messiah')
        self.assertEqual(Book.objects.get(id=self.book3.id).publication_year, 1969)
        
    def test_partial_update_view_succeeds_with_authentication(self):
        """Test that authenticated users can successfully partial update a book (PATCH)."""
        self.authenticate_user()
        data = {'author': 'Isaac Asimov II'} # Only updating the author
        response = self.client.patch(DETAIL_URL(self.book4.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify the change in the response and database
        self.assertEqual(response.data['author'], 'Isaac Asimov II')
        self.assertEqual(Book.objects.get(id=self.book4.id).author, 'Isaac Asimov II')
        # Ensure other fields are unchanged
        self.assertEqual(Book.objects.get(id=self.book4.id).title, 'Foundation')

    # =========================================================================
    # 6. DELETE VIEW (DELETE /api/books/<pk>/) - Permissions & Deletion
    # =========================================================================

    def test_delete_view_requires_authentication(self):
        """Test that anonymous users cannot delete a book."""
        initial_count = Book.objects.count()
        response = self.client.delete(DETAIL_URL(self.book2.id))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # Verify the book was NOT deleted
        self.assertEqual(Book.objects.count(), initial_count)
        self.assertTrue(Book.objects.filter(id=self.book2.id).exists())

    def test_delete_view_succeeds_with_authentication(self):
        """Test that authenticated users can successfully delete a book."""
        self.authenticate_user()
        book_id_to_delete = self.book1.id
        response = self.client.delete(DETAIL_URL(book_id_to_delete))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify the book is removed from the database
        self.assertFalse(Book.objects.filter(id=book_id_to_delete).exists())
        self.assertEqual(Book.objects.count(), 3)
