from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from eCaretaker.auth import UserBackend as check
# from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from .forms import Login, Register

# Create your views here.

def index(request):
    template = 'index.html'
    # context = {}
    return render(request, template)


def loguserin(request, authentication_form=Login):
    form = authentication_form(request.POST or None)
    # if form.is_valid():
    #     # TODO - Finish implementing login and confirm it checks the proper user table for user info
    #     print("User is a valid user")
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = check.authenticate(username=username, password = password)
    print(user)
    if user is not None:
        login(request, user)
        return render(request, 'home.html', {'name': user})
    context = {
        'form': form
    }
    return render(request, 'account/login.html', context)


def register(request, authentication_form=Register):
    form = authentication_form(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #   Display success message
        messages.success(request, "Successfully registered")
        print("user is registered")
        return HttpResponseRedirect('/login/')

    context = {
        'form': form,
    }
    messages.error(request, 'Registration failed. Please try again at another time')
    return render(request, 'account/register.html', context)


def logoff(request):
    logout(request)
    return HttpResponseRedirect('account/login/')