# Generated by Django 4.1.4 on 2023-11-19 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_pages', '0002_alter_mainpicturebanner_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]