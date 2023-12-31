# Generated by Django 4.2.6 on 2023-11-06 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NativeApp', '0011_rejectionreason'),
    ]

    operations = [
        migrations.CreateModel(
            name='HiringHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_name', models.CharField(max_length=255)),
                ('worker_name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('cost', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
