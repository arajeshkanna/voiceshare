# Generated by Django 4.2.7 on 2023-12-06 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("voiceapp", "0018_audio_audio_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="Audio_User",
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
                        related_name="Audio_name",
                        to="voiceapp.audio",
                    ),
                ),
                (
                    "User_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="User_name",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
