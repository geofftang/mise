from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for mise"""
    return render(request, 'cookbook/index.html')
