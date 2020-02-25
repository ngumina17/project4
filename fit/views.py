from django.shortcuts import render, redirect
from .models import User, Meals, Goals, Workout
from .forms import MealForm, GoalsForm, WorkoutForm
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
    workouts = Workout.objects.filter(user=request.user.id)
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
            meal = form.save(commit=False)
            meal.user_id = request.user.id
            meal = form.save()
            return redirect('meal_list')
    else:
        form = MealForm()
    return render(request, 'fit/meal_form.html', {'form': form})


@login_required
def meal_list(request):
    meals = Meals.objects.filter(user=request.user.id)
    return render(request, 'fit/meal_list.html', {'meals': meals})

@login_required
def goal_form(request):
    if request.method == 'POST':
        form = GoalsForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user_id = request.user.id
            goal = form.save()
            return redirect('goal_list')
    else:
        form = GoalsForm()
    return render(request, 'fit/goal_form.html', {'form': form})



@login_required
def goal_list(request):
    goals = Goals.objects.filter(user=request.user.id)
    return render(request, 'fit/goal_list.html', {'goals': goals})



@login_required
def workout_edit(request, id):
    workout = Workout.objects.get(id = id)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance = workout)
        if form.is_valid:
            workout = form.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm(instance = workout)
        return render(request, 'fit/workout_form.html', {'form': form})

@login_required
def meal_edit(request, id):
    meal = Meals.objects.get(id = id)
    if request.method == 'POST':
        form = MealForm(request.POST, instance = meal)
        if form.is_valid:
            workout = form.save()
            return redirect('meal_list')
    else:
        form = MealForm(instance = meal)
        return render(request, 'fit/meal_form.html', {'form': form})

@login_required
def goal_edit(request, id):
    goal = Goals.objects.get(id = id)
    if request.method == 'POST':
        form = GoalsForm(request.POST, instance = goal)
        if form.is_valid:
            goal = form.save()
            return redirect('goal_list')
    else:
        form = GoalsForm(instance = goal)
        return render(request, 'fit/goal_form.html', {'form': form})

@login_required
def meal_delete(request, pk):
    Meals.objects.get(id=pk).delete()
    return redirect('meal_list')


def goal_delete(request, id):
    Goals.objects.get(pk=id).delete()
    return redirect('goal_list')

def workout_delete(request, id):
    Workout.objects.get(id=id).delete()
    return redirect('workout_list')


