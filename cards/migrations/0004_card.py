# Generated by Django 4.1.7 on 2023-02-25 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("charas", "0001_initial"),
        ("cards", "0003_skill"),
    ]

    operations = [
        migrations.CreateModel(
            name="Card",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                (
                    "rarity",
                    models.IntegerField(
                        choices=[
                            (1, "N"),
                            (2, "Nplus"),
                            (3, "R"),
                            (4, "Rplus"),
                            (5, "Sr"),
                            (6, "Srplus"),
                            (7, "Ssr"),
                            (8, "Ssrplus"),
                        ]
                    ),
                ),
                (
                    "attribute",
                    models.IntegerField(
                        choices=[(1, "Cute"), (2, "Cool"), (3, "Passion")]
                    ),
                ),
                ("hp_min", models.IntegerField()),
                ("hp_max", models.IntegerField()),
                ("hp_bonus", models.IntegerField()),
                ("vi_min", models.IntegerField()),
                ("vi_max", models.IntegerField()),
                ("vi_bonus", models.IntegerField()),
                ("vo_min", models.IntegerField()),
                ("vo_max", models.IntegerField()),
                ("vo_bonus", models.IntegerField()),
                ("da_min", models.IntegerField()),
                ("da_max", models.IntegerField()),
                ("da_bonus", models.IntegerField()),
                (
                    "character",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="charas.character",
                    ),
                ),
                (
                    "leader_skill",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cards.leaderskill",
                    ),
                ),
                (
                    "skill",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cards.skill",
                    ),
                ),
            ],
        ),
    ]
