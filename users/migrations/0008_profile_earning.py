# Generated by Django 3.2.7 on 2021-09-15 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210914_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='earning',
            field=models.FloatField(default=0.0),
        ),
    ]
