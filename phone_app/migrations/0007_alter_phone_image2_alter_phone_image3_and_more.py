# Generated by Django 4.0 on 2023-05-02 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_app', '0006_alter_phone_image2_alter_phone_image3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='phone/images'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='phone/images'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='phone/images'),
        ),
    ]
