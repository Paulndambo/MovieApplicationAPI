# Generated by Django 4.0.4 on 2022-05-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_movie_country_movie_runtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='awards',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_rating',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_votes',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='metascore',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='plot',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rated',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='ratings',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='released',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='response',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='total_seasons',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='type',
            field=models.CharField(choices=[('movie', 'movie'), ('series', 'series'), ('episode', 'episode')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='writer',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
