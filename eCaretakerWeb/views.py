from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from .forms import Login, Register

# Create your views here.

def index(request):
    template = 'index.html'
    context = {}
    return render(request, template)

def login(request, authentication_form=Login):
    form = Login(request.POST or None)
    if form.is_valid():
        # TODO - Finish implementing login and confirm it checks the proper user table for user info
        print("User is a valid user")
    template = 'login.html'
    context = {
        'form': form
    }
    return render(request, template, context)

def register(request, authentication_form=Register):
    form = authentication_form(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #   Display success message
        messages.success(request, "Successfully registered")
        print("user is registered")
        #   TODO - Redirect properly to login after registration is successful
        return HttpResponseRedirect('login')

    context = {
        'form': form,
    }
    messages.error(request, 'Registration failed. Please try again at another time')
    return render(request, 'registration/register.html', context)

def logoff():
    #   TODO - inherit django logoff form and logic
    return