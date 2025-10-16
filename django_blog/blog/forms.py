# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
# from .models import Profile # Assumes you have defined a Profile model in blog/models.py

# # 1. Custom User Registration Form
# # Extends the default form to explicitly include the email field and
# # handles the creation of the associated Profile object.
# class CustomUserCreationForm(UserCreationForm):
#     # Set email field to be mandatory
#     email = forms.EmailField(required=True, label="Email Address")

#     class Meta(UserCreationForm.Meta):
#         model = User
#         # We only need the username and email fields for registration
#         fields = ('username', 'email')

#     def save(self, commit=True):
#         # Save the User object first
#         user = super().save(commit=False)
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#             # After creating the User, ensure the associated Profile object is created.
#             # (Note: This is also handled by a signal in models.py, but this ensures it works.)
#             if not hasattr(user, 'profile'):
#                 Profile.objects.create(user=user)
#         return user


# # 2. Profile Update Form (handles the custom Profile fields)
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         # Expose bio and profile_picture for editing
#         fields = ['bio', 'profile_picture']
#         widgets = {
#             'bio': forms.Textarea(attrs={'rows': 4}),
#         }

# # 3. User Update Form (handles the built-in User fields)
# class UserUpdateForm(UserChangeForm):
#     # Remove password fields from this form to prevent accidental password changes
#     password = None 

#     class Meta:
#         model = User
#         # Expose username and email for editing
#         fields = ('username', 'email')

#     # Since this form inherits from UserChangeForm, we override the save method
#     # to prevent it from trying to set a blank password.
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         # Ensure email is saved correctly
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user

from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm

# Placeholder: Keep your existing custom user creation form if you have one.
class CustomUserCreationForm(UserCreationForm):
    """
    If you are using a custom user model or wanted to add extra fields
    to the registration form, it would live here.
    """
    # Example: If you have extra fields, define them here.
    # No changes are needed here for the Post CRUD.
    pass

# --- NEW: Form for creating and updating blog posts ---
class PostForm(forms.ModelForm):
    """
    A ModelForm for the Post model. This form is used for both PostCreateView 
    and PostUpdateView.

    It only includes 'title' and 'content', as the 'author' and 'published_date'
    fields are set automatically in the view (views.py).
    """
    class Meta:
        model = Post
        # Define the fields the user will interact with
        fields = ['title', 'content']
        
        # Add widgets for better display in the HTML
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter a catchy title...'}),
            'content': forms.Textarea(attrs={'rows': 15, 'placeholder': 'Write your blog content here...'}),
        }
