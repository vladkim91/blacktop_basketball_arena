# Generated by Django 4.0.2 on 2022-02-12 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('height', models.IntegerField()),
                ('attributes', models.JSONField(default=dict)),
                ('tendencies', models.JSONField(default=dict)),
                ('avatar', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('image', models.CharField(max_length=300)),
                ('tier', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('wins', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='game_name', max_length=10)),
                ('game_stats', models.JSONField(default=dict)),
                ('team_one_stats', models.JSONField(default=dict)),
                ('team_two_stats', models.JSONField(default=dict)),
                ('team_one_score', models.IntegerField(default=0)),
                ('team_two_score', models.IntegerField(default=0)),
                ('team_one_squad', models.JSONField(default=dict)),
                ('team_two_squad', models.JSONField(default=dict)),
                ('date', models.DateField(blank=True, null=True)),
                ('team_one', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='team_one', to='blacktop.team')),
                ('team_two', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='team_two', to='blacktop.team')),
                ('winner', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='winner', to='blacktop.team')),
            ],
        ),
    ]
