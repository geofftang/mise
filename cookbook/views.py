from django.shortcuts import render

from .models import Recipe

# Create your views here.

def index(request):
    """The home page for mise"""
    return render(request, 'cookbook/index.html')

def recipes(request):
    """Show all recipes"""
    recipes = Recipe.objects.order_by('date_added')
    context = {'recipes': recipes}
    return render(request, 'cookbook/recipes.html', context)
