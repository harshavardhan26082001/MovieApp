# Generated by Django 3.2.3 on 2021-05-20 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_auto_20210520_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='desc',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='image',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
