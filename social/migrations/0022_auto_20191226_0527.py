# Generated by Django 2.2.6 on 2019-12-26 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0021_auto_20191226_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_rate', to=settings.AUTH_USER_MODEL),
        ),
    ]
