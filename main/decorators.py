from django.shortcuts import redirect

def rider(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.role == 'Rider':
            return view_function(request, *args, **kwargs)
        else:
            return redirect('main:provider')
    return wrapper_function

def provider(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.role == 'Provider':
            return view_function(request, *args, **kwargs)
        else:
            return redirect('main:home')
    return wrapper_function