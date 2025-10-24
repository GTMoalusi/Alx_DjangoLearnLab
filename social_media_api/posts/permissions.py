# from rest_framework import permissions

# class IsAuthorOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to only allow authors of an object to edit or delete it.
#     Read permissions are allowed to any request.
#     """
#     def has_object_permission(self, request, view, obj):
#         # Read permissions are always allowed for GET, HEAD, or OPTIONS requests.
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         # Write permissions are only allowed to the author of the post/comment.
#         # 'obj.author' references the author field on the model instance.
#         return obj.author == request.user

from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    Read permissions are allowed for any user (authenticated or not).
    
    This permission is applied on the object level (has_object_permission).
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request.
        # Check if the request method is a 'safe' method (GET, HEAD, OPTIONS).
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the post/comment.
        # We assume the model instance (obj) has an 'author' attribute.
        return obj.author == request.user
