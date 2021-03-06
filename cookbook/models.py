from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Recipe(models.Model):
    """A recipe the user wants to record"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text


class Note(models.Model):
    """Things to note about the dish or recipe"""
    recipe = models.ForeignKey(Recipe, models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text

    # class Meta:
    #     verbose_name_plural = 'entries'


class Ingredient(models.Model):
    """Ingredients required for the recipe"""
    recipe = models.ForeignKey(Recipe, models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text


class Step(models.Model):
    """Cooking steps for the recipe"""
    recipe = models.ForeignKey(Recipe, models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text
