# Generated by Django 5.0.2 on 2024-03-24 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_carasteristique2'),
    ]

    operations = [
        migrations.AddField(
            model_name='accueil',
            name='title_carasteristique2_1',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accueil',
            name='title_carasteristique2_2',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accueil',
            name='title_carasteristique2_3',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
