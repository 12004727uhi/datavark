# Generated by Django 4.1.4 on 2023-01-08 22:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ie", "0003_alter_report_source_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="record_junked",
            field=models.BooleanField(
                default=False,
                help_text="Record marked for deletion",
                verbose_name="Record junked",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="loc",
            name="coordinates",
            field=django.contrib.gis.db.models.fields.PointField(
                help_text="Coordinates of the location(s) of observation (longitude, latitude)",
                srid=4326,
                verbose_name="Observation coordinates",
            ),
        ),
    ]
