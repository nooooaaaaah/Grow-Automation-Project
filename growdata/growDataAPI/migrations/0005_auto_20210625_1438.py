# Generated by Django 3.2.4 on 2021-06-25 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('growDataAPI', '0004_plant_sensor_sensor_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='tent',
            name='lightModel',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='tent',
            name='lightOff',
            field=models.TimeField(blank=True, default=0, verbose_name='Light off'),
        ),
        migrations.AddField(
            model_name='tent',
            name='lightOn',
            field=models.TimeField(blank=True, default=0, verbose_name='Light on'),
        ),
        migrations.AddField(
            model_name='tent',
            name='numOfLights',
            field=models.IntegerField(default=1),
        ),
    ]
