# Generated by Django 4.2.8 on 2024-01-06 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icons/')),
                ('location', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PetProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='pet_icons/')),
                ('species', models.CharField(max_length=255)),
                ('breed', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('birthdate', models.DateField()),
                ('vaccination', models.BooleanField(default=False)),
                ('neutered', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
