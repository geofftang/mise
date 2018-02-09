from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Recipe
from .forms import RecipeForm
# Create your views here.


def index(request):
    """The home page for mise"""
    return render(request, 'cookbook/index.html')


@login_required
def recipes(request):
    """Show all recipes"""
    recipes = Recipe.objects.filter(owner=request.user).order_by('date_added')
    context = {'recipes': recipes}
    return render(request, 'cookbook/recipes.html', context)


@login_required
def recipe(request, recipe_id):
    """Show a single recipe and all its steps"""
    recipe = Recipe.objects.get(id=recipe_id)
    notes = recipe.note_set.order_by('-date_added')
    context = {'recipe': recipe, 'notes': notes}
    return render(request, 'cookbook/recipe.html', context)


@login_required
def new_recipe(request):
    """Add a new recipe"""
    # Rather than just = 'GET', it is safe to return a blank form for any other
    # request as well
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = RecipeForm()
    else:
        # POST data submitted; process data
        form = RecipeForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('cookbook:recipes'))

    context = {'form': form}
    return render(request, 'cookbook/new_recipe.html', context)
