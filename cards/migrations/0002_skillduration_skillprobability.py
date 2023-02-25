# Generated by Django 4.1.7 on 2023-02-25 07:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cards", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SkillDuration",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("min_duration", models.IntegerField()),
                ("max_duration", models.IntegerField()),
                ("desc", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="SkillProbability",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("min_probability", models.IntegerField()),
                ("max_probability", models.IntegerField()),
                ("desc", models.TextField()),
            ],
        ),
    ]
