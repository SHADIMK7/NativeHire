# Generated by Django 4.2.6 on 2023-10-25 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NativeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_no',
            field=models.CharField(max_length=10),
        ),
    ]
