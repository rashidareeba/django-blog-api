from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Only author can edit or delete an object.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class IsCommentAuthorOrReadOnly(permissions.BasePermission):
    """
    Only comment author can delete their comment.
    """
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return obj.author == request.user
        elif request.method in permissions.SAFE_METHODS:
            return True
        return False
