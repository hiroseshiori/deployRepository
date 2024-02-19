# Generated by Django 4.2.8 on 2024-01-21 03:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0011_chatmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdoptionPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=100)),
                ('pet_type', models.CharField(max_length=100)),
                ('pet_age', models.IntegerField()),
                ('pet_gender', models.CharField(max_length=10)),
                ('health_info', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='adoption_photos/')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adoption_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]