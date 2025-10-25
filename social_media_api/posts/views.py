from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Assuming you have a Post model defined in .models
from .models import Post 

class UserFeedView(LoginRequiredMixin, ListView):
    """
    Displays a feed of posts from the users that the currently authenticated 
    user is following, ordered by the newest post first.

    This view requires authentication via LoginRequiredMixin.
    """
    model = Post
    # The name of the context variable to hold the list of posts
    context_object_name = 'posts' 
    # Optional: Define the template name if this were a template-based application
    # template_name = 'posts/feed.html' 

    def get_queryset(self):
        """
        Filters the posts to include only those whose authors are in the 
        current user's 'following' list.
        """
        # The user object is available because of LoginRequiredMixin
        user = self.request.user
        
        # We use user.following.all() to get the queryset of users being followed.
        # We then use a Q object filter to get posts where the author is in that set.
        # This translates to an efficient SQL query (WHERE author_id IN (...))
        queryset = Post.objects.filter(
            # author__in filters posts where the author is among the users the current user follows
            author__in=user.following.all()
        ).order_by('-created_at') # Order by newest posts first

        return queryset
