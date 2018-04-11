from django import forms
from .models import Recipe, Note, Ingredient


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
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ()

    NoteFormSet = forms.inlineformset_factory(
        Recipe, Note, fields=('text',), extra=3)
