from django.db import models

# Create your models here.


class Recipe(models.Model):
    """A recipe the user wants to record"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text
