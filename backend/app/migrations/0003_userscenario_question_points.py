# Generated by Django 4.0.5 on 2022-06-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscenario',
            name='question_points',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
