# Generated by Django 4.0.4 on 2022-05-10 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='runtime',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
