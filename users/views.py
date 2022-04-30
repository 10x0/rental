from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from main.forms import RegistrationForm, UserAuthenticationForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

@unauthenticated_user
def login_view(request):

    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('/')

    if request.POST:
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                role = request.user.role
                if role == 'Rider':
                    return redirect('/')
                elif role == 'Provider':
                    return redirect('/provider/')
    else:
        form = UserAuthenticationForm()

    context['login_form'] = form
    return render(request, 'login.html', context)

@unauthenticated_user
def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            role = form.cleaned_data.get('role')
            print(role)
            User = authenticate(username=username, password=raw_password, role=role)
            login(request, User)
            if role=='Rider':
                return redirect('/rider/cars')
            elif role=='Provider':
                return redirect('/provider/')
        else:
            context['registation_form'] = form
    else:
        form = RegistrationForm()
        context['registation_form'] = form

    return render(request, 'signup.html', context)


@unauthenticated_user
def redirect_login_view(request):

    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('/')

    if request.POST:
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect(request.POST.get('next'))
    else:
        form = UserAuthenticationForm()

    context['login_form'] = form
    context['message'] = "Please log in first"
    return render(request, 'login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')