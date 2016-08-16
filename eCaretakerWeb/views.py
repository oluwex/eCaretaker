from django.shortcuts import render
from .forms import Login

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

def register(request):
    return