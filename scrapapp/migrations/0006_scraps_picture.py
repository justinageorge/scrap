# Generated by Django 4.2.7 on 2023-11-26 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapapp', '0005_remove_scraps_image_remove_scraps_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='scraps',
            name='picture',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
