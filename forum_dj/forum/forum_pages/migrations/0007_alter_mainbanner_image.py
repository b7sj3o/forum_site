# Generated by Django 4.1.4 on 2023-10-30 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_pages', '0006_alter_chosenproduct_title_alter_mainbanner_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainbanner',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Фото'),
        ),
    ]
