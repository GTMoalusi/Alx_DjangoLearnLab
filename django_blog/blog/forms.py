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

# from django import forms
# from .models import Post
# from django.contrib.auth.forms import UserCreationForm

# # Placeholder: Keep your existing custom user creation form if you have one.
# class CustomUserCreationForm(UserCreationForm):
#     """
#     If you are using a custom user model or wanted to add extra fields
#     to the registration form, it would live here.
#     """
#     # Example: If you have extra fields, define them here.
#     # No changes are needed here for the Post CRUD.
#     pass

# # --- NEW: Form for creating and updating blog posts ---
# class PostForm(forms.ModelForm):
#     """
#     A ModelForm for the Post model. This form is used for both PostCreateView 
#     and PostUpdateView.

#     It only includes 'title' and 'content', as the 'author' and 'published_date'
#     fields are set automatically in the view (views.py).
#     """
#     class Meta:
#         model = Post
#         # Define the fields the user will interact with
#         fields = ['title', 'content']
        
#         # Add widgets for better display in the HTML
#         widgets = {
#             'title': forms.TextInput(attrs={'placeholder': 'Enter a catchy title...'}),
#             'content': forms.Textarea(attrs={'rows': 15, 'placeholder': 'Write your blog content here...'}),
#         }

# from django import forms
# from .models import Post, Comment # Ensure Post is imported if other forms use it, and we definitely need Comment

# # --- Placeholder/Existing Form (If you have a CustomUserCreationForm, replace this) ---
# # NOTE: If you already have other forms in this file, make sure to merge them.
# # I'm including a placeholder for completeness.
# class CustomUserCreationForm(forms.Form): 
#     # This form should typically handle user registration fields like username, password, etc.
#     # Leaving it simple here as the focus is on CommentForm.
#     pass


# # --- New Comment Form ---
# class CommentForm(forms.ModelForm):
#     """
#     A ModelForm for the Comment model. 
#     It only exposes the 'content' field to the user.
#     """
#     # Customize the content field to use a TextArea with placeholder text
#     content = forms.CharField(
#         widget=forms.Textarea(attrs={
#             'rows': 4, # Make the input box slightly larger
#             'placeholder': 'Join the discussion... write your comment here.',
#             'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500',
#         }), 
#         label='Your Comment'
#     )
    
#     class Meta:
#         model = Comment
#         # The user only needs to input the 'content'.
#         # 'post', 'author', 'created_at', and 'updated_at' are handled in the view.
#         fields = ('content',)

# from django import forms
# from .models import Post, Comment

# # --- Post Form ---
# class PostForm(forms.ModelForm):
#     """
#     Form for creating and updating blog posts.
#     Slug and author fields are excluded as they are set automatically in the view.
#     """
#     class Meta:
#         model = Post
#         # We only let the user edit the title and body
#         fields = ('title', 'body',)
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
#         }

# # --- Comment Form ---
# class CommentForm(forms.ModelForm):
#     """
#     Form for creating comments.
#     Post, author, and date fields are excluded as they are set automatically in the view.
#     """
#     class Meta:
#         model = Comment
#         # Only the 'text' (body of the comment) is exposed to the user
#         fields = ('text',)
#         widgets = {
#             'text': forms.Textarea(attrs={
#                 'class': 'form-control', 
#                 'rows': 3, 
#                 'placeholder': 'Write your comment here...'
#             }),
#         }

from django import forms
from .models import Post, Comment

# --- Post Form ---
class PostForm(forms.ModelForm):
    """
    Form for creating and updating blog posts.
    Slug and author fields are excluded as they are set automatically in the view.
    """
    class Meta:
        model = Post
        # Corrected field name: using 'content' instead of 'body'
        fields = ('title', 'content',) 
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # Corrected field name: using 'content' instead of 'body'
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
        }

# --- Comment Form ---
class CommentForm(forms.ModelForm):
    """
    Form for creating comments.
    Post, author, and date fields are excluded as they are set automatically in the view.
    """
    class Meta:
        model = Comment
        # Only the 'text' (body of the comment) is exposed to the user
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Write your comment here...'
            }),
        }
