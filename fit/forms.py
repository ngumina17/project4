from django import forms
from .models import User, Meals, Goals, Workout

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'location', 'photo_url',)

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'author', 'content', 'photo_url',)

class SearchBar(forms.Form):
        fields = ('search')