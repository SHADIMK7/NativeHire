# Generated by Django 4.2.6 on 2023-11-04 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NativeApp', '0009_alter_customer_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_no',
            field=models.CharField(max_length=10),
        ),
    ]
