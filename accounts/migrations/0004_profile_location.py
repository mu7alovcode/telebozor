# Generated by Django 4.0 on 2023-05-03 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]