from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def index(request):
    template = 'home/index.html'
    print(request.user.is_authenticated())
    if not request.user.is_authenticated():
        messages.error(request, 'Please login to continue')
        return redirect('/login')
    return render(request, template)