from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField()
    
    def __str__(self):
        return self.name

class Meals(models.Model):
    Meal_Type = models.CharField(max_length=50)
    calories = models.CharField(max_length=50)
    contents = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')

    def __str__(self):
        return self.Meal_Type

class Goals(models.Model):
    contents = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')

    def __str__(self):
        return self.contents

class Workout(models.Model):
    completed = models.TextField()
    notes=models.CharField(default='', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    
    def __str__(self):
        return self.completed