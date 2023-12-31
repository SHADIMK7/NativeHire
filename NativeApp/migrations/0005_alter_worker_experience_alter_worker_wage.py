# Generated by Django 4.2.6 on 2023-11-02 17:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NativeApp', '0004_rename_message_notification_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='experience',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='worker',
            name='wage',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
