# Generated by Django 4.2.8 on 2024-02-18 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_nutritionpost_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petprofile',
            name='gender',
            field=models.CharField(choices=[('male', 'オス'), ('female', 'メス')], max_length=10),
        ),
    ]
