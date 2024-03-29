# Generated by Django 3.2.4 on 2021-07-14 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('growDataAPI', '0002_rename_lightmodel_tent_lightwatts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='plant',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='growDataAPI.plant'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='tent',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='growDataAPI.tent'),
        ),
    ]
