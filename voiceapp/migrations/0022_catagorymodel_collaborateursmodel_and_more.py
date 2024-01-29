# Generated by Django 5.0 on 2023-12-14 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("voiceapp", "0021_alter_audio_user_audio_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CatagoryModel",
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
                "verbose_name_plural": "Tous les audios",
            },
        ),
        migrations.CreateModel(
            name="CollaborateursModel",
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
                "verbose_name_plural": "Collaborateurs",
            },
        ),
        migrations.CreateModel(
            name="Fichiers_reçusModel",
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
                "verbose_name_plural": "Fichiers_reçus",
            },
        ),
    ]
