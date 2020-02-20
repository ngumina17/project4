from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'photo_url',)

# class MealForm(forms.ModelForm):
#     class Meta:
#         model = Meals
#         fields = ('Meal_Type', 'contents', 'calories',)

# class GoalsForm(forms.ModelForm):
#         model = Goals
#         fields = ('contents',) 

# class WorkoutForm(forms.ModelForm):
#         model = Workout
#         fields = ('completed', 'notes',)