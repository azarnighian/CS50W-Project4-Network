# Generated by Django 3.0.8 on 2020-11-17 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_auto_20201109_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='liked_posts',
            field=models.ManyToManyField(blank=True, related_name='likers', to='network.Posts'),
        ),
    ]