# Generated by Django 2.2.6 on 2019-12-21 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0016_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='userposts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userpost_comment', to='social.UserPosts'),
        ),
    ]
