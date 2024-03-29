from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages as login_errors

def login_view(request):
    login_page = True

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if len(username) > 20:
            return redirect('login')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        login_errors.error(request, "Username or password does not match. Try again")
        return redirect('login')


    context = {'login_page' : login_page, 'errors' : login_errors}
    return render(request, 'authenti/login.html', context)




def register_view(request):
    user_creation_form = UserCreationForm()
    login_page = False

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        user_creation_form = UserCreationForm(request.POST)
        
        if user_creation_form.is_valid():
            user = user_creation_form.save()
            username = user_creation_form.cleaned_data.get('username')
            password = user_creation_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            login_errors.error(request, "Something went wrong. Try again")

    context = {'user_creation_form': user_creation_form}
    return render(request, 'authenti/register.html', context)


@login_required(login_url = 'login')
def logout_view(request):
    logout(request)

    context = {}
    return redirect('login')