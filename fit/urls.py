# fit/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_dashboard, name ='user_dashboard'),
    path('user/new', views.user_form, name ='user_form'),
    path('workouts/', views.workout_list, name='workout_list'),
    path('meals/', views.meal_list, name='meal_list'),
    path('workout/new/', views.workout_form, name='workout_form'),
    path('meals/new/', views.meal_form, name='meal_form'),
    path('goals/new/', views.goal_form, name='goal_form'),
    path('goals/', views.goal_list, name='goal_list'),
]