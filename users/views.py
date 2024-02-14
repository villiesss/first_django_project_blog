from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import UserRegistrationForm
from blog.settings import LOGIN_REDIRECT_URL
from main.views import menu


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            context = {'new_user': new_user, 'menu': menu }
            return render(request, 'users/register_done.html', context=context)

    user_form = UserRegistrationForm()
    context = {'user_form': user_form, 'menu': menu }
    return render(request, 'users/register.html', context=context)


def log_in(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            url = request.GET.get('next', LOGIN_REDIRECT_URL)
            return redirect(url)
    return render(request, 'users/login.html', {'form': form, 'menu': menu})

def log_out(request):
    logout(request)
    url = reverse('main:post_list')
    return redirect(url)


def get_user_info(request, pk):
    user = User.objects.get(pk=pk)
    context = {"user":user, "menu":menu}
    return render(request, "users/user.html", context=context)


def pef():
    pass

def xeru():
    pass