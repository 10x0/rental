from django.shortcuts import redirect

def unauthenticated_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main:home' if request.user.role=='Rider' else 'main:provider')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_function