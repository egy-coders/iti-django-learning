from django.http import HttpResponseForbidden
from functools import wraps


def role_required(role):
    def decorator(view_func):
        @wraps 
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("You do not have permission to access this page")
        return _wrapped_view
    return decorator
