# Generated by Django 4.2.8 on 2023-12-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subthemes',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
