from django.shortcuts import render, redirect
from .models import User, Meals, Goals, Workout
# from .forms import UserForm, MealForm, GoalsForm, WorkoutForm


# Create your views here.
def user_dashboard(request):
    users = User.objects.all()
    return render(request, 'fit/user_dashboard.html', {'users': users})

# def user_dashboard(request):
#     user = User.objects.get()
#     return render(request, 'fit/user_dashboard.html', {'user': user})

