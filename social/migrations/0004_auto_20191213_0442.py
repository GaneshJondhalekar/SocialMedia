# Generated by Django 2.2.6 on 2019-12-13 04:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20191213_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='friends', to=settings.AUTH_USER_MODEL),
        ),
    ]
