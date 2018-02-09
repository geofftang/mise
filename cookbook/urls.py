"""Defines URL patterns for cookbook"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    url(r'^recipes/$', views.recipes, name='recipes'),
    url(r'^recipes/(?P<recipe_id>\d+)/$', views.recipe, name='recipe'),
    url(r'^new_recipe/$', views.new_recipe, name="new_recipe"),
]
