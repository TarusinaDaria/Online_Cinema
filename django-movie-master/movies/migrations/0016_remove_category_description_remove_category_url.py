# Generated by Django 4.0.6 on 2022-07-10 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_category_movie_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='url',
        ),
    ]
