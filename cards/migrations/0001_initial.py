# Generated by Django 4.1.7 on 2023-02-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LeaderSkill",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("desc", models.TextField()),
            ],
        ),
    ]
