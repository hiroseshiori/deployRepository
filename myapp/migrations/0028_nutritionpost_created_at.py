# Generated by Django 4.2.8 on 2024-02-17 16:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_alter_nutritionpost_symptom'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutritionpost',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]