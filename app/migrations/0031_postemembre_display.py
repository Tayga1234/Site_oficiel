# Generated by Django 5.0.2 on 2024-03-26 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_postemembre_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='postemembre',
            name='display',
            field=models.CharField(default=200, max_length=10),
            preserve_default=False,
        ),
    ]
