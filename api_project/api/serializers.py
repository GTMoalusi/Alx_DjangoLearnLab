from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """
    A serializer for the Book model.
    This converts Book model instances to JSON format.
    """
    class Meta:
        model = Book
        fields = '__all__'