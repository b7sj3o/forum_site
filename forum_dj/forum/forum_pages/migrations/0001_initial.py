# Generated by Django 4.1.4 on 2023-10-30 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Тайтл')),
                ('text', models.TextField(verbose_name='Повідомлення')),
            ],
        ),
    ]
