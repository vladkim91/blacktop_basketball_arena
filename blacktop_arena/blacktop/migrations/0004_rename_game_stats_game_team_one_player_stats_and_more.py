# Generated by Django 4.0.2 on 2022-02-14 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blacktop', '0003_auto_20220214_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='game_stats',
            new_name='team_one_player_stats',
        ),
        migrations.RemoveField(
            model_name='game',
            name='team_one',
        ),
        migrations.RemoveField(
            model_name='game',
            name='team_two',
        ),
        migrations.RemoveField(
            model_name='game',
            name='winner',
        ),
        migrations.AddField(
            model_name='game',
            name='team_two_player_stats',
            field=models.JSONField(default=dict),
        ),
    ]
