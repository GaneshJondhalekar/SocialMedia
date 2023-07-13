# Generated by Django 2.2.6 on 2019-12-13 04:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0002_auto_20191210_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='friends',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
