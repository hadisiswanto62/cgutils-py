# Generated by Django 4.1.7 on 2023-03-19 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_team"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="leader",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="leader",
                to="users.ownedcard",
            ),
        ),
    ]
