# Generated by Django 4.2.7 on 2023-12-06 14:50

from django.db import migrations, models
import voiceapp.models


class Migration(migrations.Migration):

    dependencies = [
        ("voiceapp", "0017_remove_audio_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="audio",
            name="audio_file",
            field=models.FileField(
                blank=True, null=True, upload_to=voiceapp.models.getFileName
            ),
        ),
    ]
