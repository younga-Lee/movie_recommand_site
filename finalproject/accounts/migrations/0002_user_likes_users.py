# Generated by Django 3.2.18 on 2023-05-25 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_remove_movie_likes_users'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='likes_users',
            field=models.ManyToManyField(related_name='likes', to='movies.Movie'),
        ),
    ]
