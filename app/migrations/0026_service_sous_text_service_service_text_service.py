# Generated by Django 5.0.2 on 2024-03-25 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='sous_text_service',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='text_service',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
