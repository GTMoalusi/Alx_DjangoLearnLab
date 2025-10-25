from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

# Get the custom user model defined in settings.AUTH_USER_MODEL
CustomUser = get_user_model()

# --- Class-Based Views for Follow Functionality ---

class FollowUserView(LoginRequiredMixin, View):
    """
    Handles POST request to follow a user by their primary key (pk).
    Requires the user to be authenticated.
    """
    def post(self, request, pk, *args, **kwargs):
        # 1. Try to retrieve the target user. Returns a 404 if not found.
        try:
            user_to_follow = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return JsonResponse({'detail': 'User not found.'}, status=404)

        # 2. Prevent a user from following themselves
        if request.user.pk == user_to_follow.pk:
            return JsonResponse({'detail': 'Cannot follow yourself.'}, status=400)
        
        # 3. Add the user to the current user's 'following' list
        # If the user is already following, .add() does nothing.
        request.user.following.add(user_to_follow)
        
        return JsonResponse(
            {'status': f'Successfully following {user_to_follow.username}.'}, 
            status=200
        )


class UnfollowUserView(LoginRequiredMixin, View):
    """
    Handles POST request to unfollow a user by their primary key (pk).
    Requires the user to be authenticated.
    """
    def post(self, request, pk, *args, **kwargs):
        # 1. Try to retrieve the target user. Returns a 404 if not found.
        try:
            user_to_unfollow = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return JsonResponse({'detail': 'User not found.'}, status=404)
        
        # 2. Remove the user from the current user's 'following' list
        # If the user is not following, .remove() does nothing.
        request.user.following.remove(user_to_unfollow)

        return JsonResponse(
            {'status': f'Successfully unfollowed {user_to_unfollow.username}.'}, 
            status=200
        )

# NOTE: You should ensure any other necessary views (like profile, etc.) are also in this file.
