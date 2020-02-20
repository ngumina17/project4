from django.contrib import admin
from .models import User, Workout, Goals, Meals

# Register your models here.
admin.site.register(User)
admin.site.register(Workout)
admin.site.register(Goals)
admin.site.register(Meals)