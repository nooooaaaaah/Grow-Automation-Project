# Generated by Django 3.2.4 on 2021-07-23 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('growDataAPI', '0004_auto_20210714_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tent',
            name='lightOff',
        ),
        migrations.RemoveField(
            model_name='tent',
            name='lightOn',
        ),
        migrations.AlterField(
            model_name='tent',
            name='lightWatts',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
