# fit/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_dashboard, name ='user_dashboard'),
    path('workouts/', views.workout_list, name='workout_list'),
    path('meals/', views.meal_list, name='meal_list'),
    path('workout/new/', views.workout_form, name='workout_form'),
    path('meals/new/', views.meal_form, name='meal_form'),
    path('goals/new/', views.goal_form, name='goal_form'),
    path('goals/', views.goal_list, name='goal_list'),
    path('workout/edit/<int:id>', views.workout_edit, name='workout_edit'),
    path('meal/edit/<int:id>', views.meal_edit, name='meal_edit'),
    path('goal/edit/<int:id>', views.goal_edit, name='goal_edit'),
    
]
