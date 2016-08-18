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
        return HttpResponseRedirect('login')

    context = {
        'form': form,
    }
    messages.error(request, 'Not successfully created')
    return render(request, 'registration/register.html', context)