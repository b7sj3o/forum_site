# Generated by Django 4.1.4 on 2023-11-22 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpicturebanner',
            name='image',
            field=models.ImageField(upload_to='forum_pages/img/banners', verbose_name='Фото'),
        ),
    ]