from functools import wraps
from django.http import Http404


def admin_required(view_func):
    """
    Simple decorator that checks if user is logged in and belongs to 'admin' group.
    If not, raises Http404 to make it appear like the page doesn't exist.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Check if user is authenticated and belongs to admin group
        if (request.user.is_authenticated and 
            request.user.groups.filter(name='admin').exists()):
            # User is logged in and is admin, allow access
            return view_func(request, *args, **kwargs)
        else:
            # User is not logged in or not admin, raise 404
            raise Http404("Page not found")
    
    return wrapper


# Usage example:
"""
from django.shortcuts import render
from .decorators import admin_required

@admin_required
def admin_panel(request):
    return render(request, 'admin_panel.html')

@admin_required
def admin_settings(request):
    return render(request, 'admin_settings.html')
"""