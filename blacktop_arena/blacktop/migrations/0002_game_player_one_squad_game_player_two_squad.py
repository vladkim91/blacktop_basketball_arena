# Generated by Django 4.0.2 on 2022-02-08 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blacktop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='player_one_squad',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='game',
            name='player_two_squad',
            field=models.JSONField(default=dict),
        ),
    ]
