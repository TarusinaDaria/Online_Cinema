# Generated by Django 4.0.6 on 2022-07-10 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_director_alter_actor_options_movie_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ManyToManyField(related_name='category_director', to='movies.category', verbose_name='категории'),
        ),
    ]
