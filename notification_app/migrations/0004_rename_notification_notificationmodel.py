# Generated by Django 4.2.2 on 2023-08-29 10:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notification_app', '0003_alter_notification_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notification',
            new_name='NotificationModel',
        ),
    ]
