# Generated by Django 3.2.3 on 2021-05-20 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_auto_20210520_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='image',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='offer',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='price',
        ),
    ]
