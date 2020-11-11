# Generated by Django 3.0.8 on 2020-11-02 19:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_auto_20201029_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(default=0, related_name='_user_followers_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(default=0, related_name='_user_following_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
