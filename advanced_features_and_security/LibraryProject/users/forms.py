# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CustomUser

# # Form for creating a new custom user.
# class CustomUserCreationForm(UserCreationForm):
#     """A custom form for creating a new user."""

#     class Meta:
#         # Define the model to use.
#         model = CustomUser
#         # Define the fields to display in the form.
#         fields = ("email", "username")

# # Form for changing an existing custom user.
# class CustomUserChangeForm(UserChangeForm):
#     """A custom form for updating an existing user."""

#     class Meta:
#         # Define the model to use.
#         model = CustomUser
#         # Define the fields to display in the form.
#         fields = ("email", "username")

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)
