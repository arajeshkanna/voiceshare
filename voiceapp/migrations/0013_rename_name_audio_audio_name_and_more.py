# Generated by Django 4.2.7 on 2023-12-06 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("voiceapp", "0012_audio"),
    ]

    operations = [
        migrations.RenameField(
            model_name="audio",
            old_name="name",
            new_name="Audio_name",
        ),
        migrations.RenameField(
            model_name="catagory",
            old_name="name",
            new_name="Catagory_name",
        ),
        migrations.CreateModel(
            name="Catagory_Audio",
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
                (
                    "Audio_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="name",
                        to="voiceapp.audio",
                    ),
                ),
                (
                    "Catagory_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="name",
                        to="voiceapp.catagory",
                    ),
                ),
            ],
        ),
    ]
