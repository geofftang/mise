from django.contrib import admin
from cookbook.models import Recipe, Note, Ingredient, Step

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Note)
admin.site.register(Ingredient)
admin.site.register(Step)
