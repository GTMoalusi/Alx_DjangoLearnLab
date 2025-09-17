# users/admin.py

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser

# # Register the CustomUser model with the custom admin class.
# class CustomUserAdmin(UserAdmin):
#     """Custom User Admin class."""
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ["email", "username", "is_staff"]
#     fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("email",)}),)
#     add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("email",)}),)

# # Register the CustomUser model in the admin site.
# admin.site.register(CustomUser, CustomUserAdmin)

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     # Add custom fields for the add user form
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('age',)}),
#     )
#     # Customize the fieldsets for editing an existing user
#     fieldsets = UserAdmin.fieldsets + (
#         ('Custom Fields', {'fields': ('age',)}),
#     )
#     # The error is likely in this section.
#     # Check for a duplicate field name in the 'fields' list below.
#     fieldsets = (
#         ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
#         ('User Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important Dates', {'fields': ('last_login', 'date_joined')}),
#         # This is likely the problematic fieldset.
#         # Ensure 'field1' and 'field2' are unique and don't appear anywhere else
#         # in this list. For example, 'field1' should not be duplicated.
#         ('Example Group', {'fields': ('field1', 'field2')}),
#         ('Another Group', {'fields': ('some_field', 'field_to_fix')}),
#         # Make sure there are no duplicates
#     )

# admin.site.register(CustomUser, CustomUserAdmin)

# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm

# CustomUser = get_user_model()

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ["email", "is_staff"]
#     fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("email",)}),)
#     add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("email",)}),)

# admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "is_staff"]
    list_filter = ["is_staff", "is_superuser", "is_active", "groups"]
    search_fields = ["email"]
    ordering = ["email"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name")}),
        (("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password", "password2"),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
