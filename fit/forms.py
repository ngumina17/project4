from django import forms
from .models import User, Goals, Meals, Workout

class MealForm(forms.ModelForm):
    class Meta:
        model = Meals
        fields = ('Meal_Type', 'contents', 'calories',)


class GoalsForm(forms.ModelForm):
    class Meta:
        model = Goals
        fields = ('contents',)


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('completed', 'notes',)
        
