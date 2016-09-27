from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'Locations/index.html')

def search(request, type):
    if type not in ['Duplex', 'Face Me I Face you', 'Bungalow', 'Flat']:
        messages.error(request, message="Invalid House type")
        return redirect("/eCaretaker/")