# Generated by Django 4.2.8 on 2023-12-24 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum_pages', '0002_subthemes_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopAgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('banner', models.ImageField(blank=True, upload_to='forum_pages/img/top_agency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
