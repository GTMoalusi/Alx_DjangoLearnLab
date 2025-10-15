from django.contrib.auth.forms import UserCreationForm

# We'll use Django's built-in UserCreationForm for a simple registration.
class CustomUserCreationForm(UserCreationForm):
    """
    A custom form inheriting from Django's built-in UserCreationForm.
    This provides all necessary fields (username, password, password confirmation)
    for registering a new user.
    """
    class Meta(UserCreationForm.Meta):
        # We explicitly list the fields here, though simply inheriting is enough for now.
        fields = UserCreationForm.Meta.fields
