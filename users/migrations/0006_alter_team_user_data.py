# Generated by Django 4.1.7 on 2023-03-19 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_team_user_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="user_data",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.userdata"
            ),
        ),
    ]
