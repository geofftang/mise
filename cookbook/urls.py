"""Defines URL patterns for cookbook"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # Page listing all of a user's recipes
    url(r'^recipes/$', views.recipes, name='recipes'),
<<<<<<< HEAD
    # Pages for each of a user's recipes
    url(r'^recipes/(?P<recipe_id>\d+)/$', views.recipe, name='recipe'),
    # Page for adding a new recipe
=======
    url(r'^recipes/(?P<recipe_id>\d+)/$', views.recipe, name='recipe'),
>>>>>>> 022ce368dc776a2f97ea5acb8c0d43bba97d2c66
    url(r'^new_recipe/$', views.new_recipe, name="new_recipe"),
    # Page for adding a new note
    url(r'^new_note/(?P<recipe_id>\d+)/$', views.new_note, name="new_note"),
    # Page for adding a new note
    url(r'^edit_note/(?P<note_id>\d+)/$', views.edit_note, name="edit_note"),

]
