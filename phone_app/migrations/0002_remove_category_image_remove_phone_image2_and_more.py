# Generated by Django 4.0 on 2023-04-30 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phone_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='image4',
        ),
    ]
