# Generated by Django 4.2.8 on 2024-04-01 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_pages', '0002_agencyjoborganization_alter_basetheme_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='basetheme',
            name='link',
            field=models.URLField(default='', verbose_name='Посилання'),
            preserve_default=False,
        ),
    ]