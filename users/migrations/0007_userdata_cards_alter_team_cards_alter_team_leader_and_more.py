# Generated by Django 4.1.7 on 2023-03-19 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cards", "0007_alter_card_options"),
        ("users", "0006_alter_team_user_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="userdata",
            name="cards",
            field=models.ManyToManyField(to="cards.card"),
        ),
        migrations.AlterField(
            model_name="team",
            name="cards",
            field=models.ManyToManyField(related_name="nonleaders", to="cards.card"),
        ),
        migrations.AlterField(
            model_name="team",
            name="leader",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="leader",
                to="cards.card",
            ),
        ),
        migrations.DeleteModel(
            name="OwnedCard",
        ),
    ]
