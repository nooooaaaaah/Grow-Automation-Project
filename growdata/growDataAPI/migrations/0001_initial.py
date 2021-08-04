# Generated by Django 3.2.4 on 2021-07-14 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('name', models.CharField(max_length=60)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('name', models.CharField(max_length=60)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('seed', models.BooleanField(default=False)),
                ('clone', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('name', models.CharField(max_length=60)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='growDataAPI.plant')),
            ],
        ),
        migrations.CreateModel(
            name='Tent',
            fields=[
                ('name', models.CharField(max_length=60)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lightModel', models.IntegerField(blank=True, default=None, null=True)),
                ('numOfLights', models.IntegerField(default=1)),
                ('lightOn', models.TimeField(blank=True, default=0, verbose_name='Light on')),
                ('lightOff', models.TimeField(blank=True, default=0, verbose_name='Light off')),
                ('cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='growDataAPI.cycle')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor_Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('temp', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='growDataAPI.sensor')),
            ],
        ),
        migrations.AddField(
            model_name='sensor',
            name='tent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='growDataAPI.tent'),
        ),
        migrations.AddField(
            model_name='plant',
            name='tent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='growDataAPI.tent'),
        ),
    ]
