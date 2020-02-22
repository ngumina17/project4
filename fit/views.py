from django.shortcuts import render, redirect
from .models import User, Meals, Goals, Workout
from .forms import UserForm, MealForm, GoalsForm, WorkoutForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def user_dashboard(request):
    users = User.objects.all()
    return render(request, 'fit/user_dashboard.html', {'users': users})


def user_list(request):
    users = User.objects.all()
    return render(request, 'fit/user_list.html', {'users': users})


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_dashboard', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'fit/user_form.html', {'form': form})

@login_required
def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, 'fit/workout_list.html', {'workouts': workouts})

@login_required
def workout_form(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST, request.FILES)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user_id = request.user.id
            workout.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm()
    return render(request, 'fit/workout_form.html', {'form': form})

@login_required
def meal_form(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save()
            return redirect('meal_list', pk=meal.pk)
    else:
        form = MealForm()
    return render(request, 'fit/meal_form.html', {'form': form})

@login_required
def goal_form(request):
    if request.method == 'POST':
        form = GoalsForm(request.POST)
        if form.is_valid():
            goal = form.save()
            return redirect('goal_list', pk=goal.pk)
    else:
        form = GoalsForm()
    return render(request, 'fit/goal_form.html', {'form': form})


