from django.http import HttpResponse, response
from django.shortcuts import redirect


# decorators to redirect to home page in login user try to login
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


# decorators for the authenticates users
def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are Not Authorized to View this page!!!")

            return view_func(request, *args, **kwargs)

        return wrapper_func

    return decorator
