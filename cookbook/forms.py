from django import forms
from .models import Recipe, Note

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['text']
        labels = {'text': ''}


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
