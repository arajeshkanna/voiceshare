# Generated by Django 5.0 on 2023-12-22 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("voiceapp", "0024_alter_audio_group_group_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Audio_attribueModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Audio_attribue",
            },
        ),
    ]
