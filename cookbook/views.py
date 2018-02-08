from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Recipe
from .forms import RecipeForm
# Create your views here.

def index(request):
    """The home page for mise"""
    return render(request, 'cookbook/index.html')

def recipes(request):
    """Show all recipes"""
    recipes = Recipe.objects.order_by('date_added')
    context = {'recipes': recipes}
    return render(request, 'cookbook/recipes.html', context)

def new_recipe(request):
    """Add a new recipe"""
    #Rather than just = 'GET', it is safe to return a blank form for any other
    #request as well
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = RecipeForm()
    else:
        # POST data submitted; process data
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cookbook:recipes'))

    context = {'form': form}
    return render(request, 'cookbook/new_recipe.html', context)
