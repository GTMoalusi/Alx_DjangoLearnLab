# from django.contrib import admin
# from .models import Book

# # Register your models here.
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#    list_display = ("title", "author", "publication_year")
#    list_filter = ("author", "publication_year")
#    search_fields = ("title", "author")
#    # date_hierarchy = "published_date"

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# # from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     """
#     Admin configuration for the CustomUser model.
#     This class adds the new fields to the admin form and display lists.
#     """
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('date_of_birth', 'profile_photo')}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('date_of_birth', 'profile_photo')}),
#     )
    
# # Unregister the default User model
# admin.site.unregister(CustomUser)
# # Register the new CustomUser model with the custom admin class
# admin.site.register(CustomUser, CustomUserAdmin)

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# from users.models import CustomUser
# from users.forms import CustomUserCreationForm, CustomUserChangeForm

# class CustomUserAdmin(UserAdmin):
#    add_form = CustomUserCreationForm
#    form = CustomUserChangeForm
#    model = CustomUser
#    list_display = ["email", "username",]

# admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin

# No CustomUser imports here anymore
# from users.models import CustomUser
# from users.forms import CustomUserCreationForm, CustomUserChangeForm

# No CustomUserAdmin class here anymore
# class CustomUserAdmin(UserAdmin):
#    ...

# No registration here anymore
# admin.site.register(CustomUser, CustomUserAdmin)
