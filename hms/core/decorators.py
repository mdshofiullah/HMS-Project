from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

def role_required(*allowed_roles):
    """
    Decorator to restrict access to views based on user role.
    Usage: @role_required('ADMIN', 'DOCTOR')
    """
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                if request.user.role in allowed_roles or request.user.is_superuser:
                    return view_func(request, *args, **kwargs)
                return HttpResponseForbidden("You don't have permission to access this page.")
            return redirect('login')
        return wrapper
    return decorator