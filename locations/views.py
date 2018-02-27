from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'Locations/index.html')


#   Todo: Implement house search by location

