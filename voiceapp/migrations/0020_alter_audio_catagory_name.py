# Generated by Django 5.0 on 2023-12-11 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("voiceapp", "0019_audio_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audio",
            name="Catagory_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="voiceapp.catagory"
            ),
        ),
    ]
