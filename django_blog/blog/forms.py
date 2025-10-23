from django import forms
from .models import Post, Comment
from taggit.forms import TagField 

class PostForm(forms.ModelForm):
    # We are adding the 'tags' field here
    tags = TagField(required=False, help_text="Enter tags separated by commas.")

    class Meta:
        model = Post
        # Post model uses 'title' and 'content'
        fields = ('title', 'content', 'tags')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'create-form-input'}),
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # FIX: Using 'text' to match the field in blog/models.py
        fields = ('text',)

        widgets = {
            # FIX: Using 'text' as the widget key
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea', 'placeholder': 'Write your comment here...'}),
        }
