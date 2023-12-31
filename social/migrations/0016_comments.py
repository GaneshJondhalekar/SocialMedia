# Generated by Django 2.2.6 on 2019-12-19 04:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0015_auto_20191218_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_comment', to=settings.AUTH_USER_MODEL)),
                ('userposts', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userpost_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
