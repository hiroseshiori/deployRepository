# Generated by Django 4.2.8 on 2024-02-13 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_adoptionpost_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptionpost',
            name='address',
            field=models.CharField(default='Unknown', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adoptionpost',
            name='reason',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
