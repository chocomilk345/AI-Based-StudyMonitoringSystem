# Generated by Django 4.2.13 on 2024-05-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_behaviorlog_pose'),
    ]

    operations = [
        migrations.AddField(
            model_name='behaviorlog',
            name='pose_bad',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='behaviorlog',
            name='pose_good',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
