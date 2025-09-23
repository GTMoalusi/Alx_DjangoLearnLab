from django.contrib import admin
from .models import Book

# Register your models here.
# This line tells Django's admin site to include the 'Book' model.
admin.site.register(Book)
