# Generated by Django 3.2.3 on 2021-05-20 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='subs',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
