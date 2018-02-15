from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Recipe, Note
from .forms import RecipeForm, NoteForm

# Relevant Functions


# Make sure the recipe belongs to the current user
def check_recipe_owner(recipe, request):
    if recipe.owner != request.user:
        raise Http404


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
    recipe = get_object_or_404(Recipe, id=recipe_id)
    check_recipe_owner(recipe, request)

    notes = recipe.note_set.order_by('-date_added')
    context = {'recipe': recipe, 'notes': notes}
    return render(request, 'cookbook/recipe.html', context)


@login_required
def new_recipe(request):
    """Add a new recipe"""
    # Rather than just = 'GET', it is safe to return a blank form for any other
    # request as well
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = RecipeForm()
    else:
        # POST data submitted; process data
        form = RecipeForm(request.POST)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.owner = request.user
            new_recipe.save()
            return HttpResponseRedirect(reverse('cookbook:recipes'))

    context = {'form': form}
    return render(request, 'cookbook/new_recipe.html', context)


@login_required
def new_note(request, recipe_id):
    """Add a new note to a recipe"""
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = NoteForm()
    else:
        # POST data submitted; process data
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.recipe = recipe
            new_note.save()
            return HttpResponseRedirect(
                reverse('cookbook:recipe', args=[recipe_id]))

    context = {'recipe': recipe, 'form': form}
    return render(request, 'cookbook/new_note.html', context)


@login_required
def edit_note(request, note_id):
    """Edit an existing note"""
    note = get_object_or_404(Note, id=note_id)
    recipe = note.recipe
    check_recipe_owner(recipe, request)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current note
        form = NoteForm(instance=note)
    else:
        # POST data submitted; process data
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('cookbook:recipe', args=[recipe.id]))

    context = {'recipe': recipe, 'form': form}
    return render(request, 'cookbook/edit_note.html', context)
