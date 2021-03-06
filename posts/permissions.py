from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method is permissions.SAFE_METHODS:
            return True
        return obj.author == request.user