# Generated by Django 3.0.3 on 2020-02-25 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0003_workout_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goals',
            name='contents',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='meals',
            name='Meal_Type',
            field=models.CharField(max_length=50),
        ),
    ]
