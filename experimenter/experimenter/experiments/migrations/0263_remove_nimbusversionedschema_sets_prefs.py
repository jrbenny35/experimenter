# Generated by Django 3.2.23 on 2024-02-06 22:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0262_nimbusexperiment_risk_message"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="nimbusversionedschema",
            name="sets_prefs",
        ),
    ]