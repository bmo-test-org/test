# Generated by Django 4.0.5 on 2022-06-22 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='avg_mu',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='template_scenario_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='template_scenario_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='username',
            field=models.TextField(blank=True, null=True),
        ),
    ]
