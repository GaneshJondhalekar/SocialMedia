# Generated by Django 2.2.6 on 2019-12-25 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0019_recentsearch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_rate', to=settings.AUTH_USER_MODEL)),
                ('userposts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userpost_rate', to='social.UserPosts')),
            ],
        ),
    ]
