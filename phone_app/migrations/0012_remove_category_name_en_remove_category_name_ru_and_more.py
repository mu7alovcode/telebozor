# Generated by Django 4.0 on 2023-05-11 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phone_app', '0011_category_name_en_category_name_ru_category_name_uz_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_uz',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='body_en',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='body_ru',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='body_uz',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='title_uz',
        ),
    ]