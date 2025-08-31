from django.contrib import admin
from . models import Book

# Register your models here.
@admin.register(Book)
class BooKAdmin(admin.ModelAdmin):
   list_display = ("title", "author", "publication_date")
   list_filter = ("author", "publication_date")
   search_fields = ("title", "author")
   date_hierarchy = "publication_date"