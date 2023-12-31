# Generated by Django 4.2.7 on 2023-11-24 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scraps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('user', models.CharField(max_length=200)),
            ],
        ),
    ]
