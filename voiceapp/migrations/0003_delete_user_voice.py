# Generated by Django 4.2.7 on 2023-11-30 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("voiceapp", "0002_alter_user_voice_voice_file"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User_Voice",
        ),
    ]