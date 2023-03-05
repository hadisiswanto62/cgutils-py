import logging
import sqlite3
from django.core.management.base import BaseCommand

from data_updater.network import request_card_icon
from data_updater.utils import paths, files
from data_updater import gamedbparser, updater
from charas.models import Character
from cards.models import LeaderSkill, SkillDuration, SkillProbability, Skill, Card

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--nodl",
            action="store_true",
            help="Use existing game DB instead of downloading a new one",
        )

    def handle(self, *args, **options):
        if not options["nodl"]:
            logger.info("Downloading game DB")
            updater.update_manifest()
            updater.update_master()
        else:
            logger.info("Populating db using existing game DB")
        if not paths.MASTERDB_PATH.exists():
            logger.error(f"Master DB is not found at {paths.MASTERDB_PATH}. Exiting")
            return
        masterdb_conn = sqlite3.connect(paths.MASTERDB_PATH)
        masterdb_conn.row_factory = sqlite3.Row

        unique_fields = set(["id"])
        # _state is django internal field
        non_updatable_fields = unique_fields.union(["_state"])

        characters = gamedbparser.parse_characters(masterdb_conn)
        if len(characters) > 0:
            updatable_fields = set(characters[0].__dict__).difference(
                non_updatable_fields
            )
            Character.objects.bulk_create(
                characters,
                update_conflicts=True,
                update_fields=updatable_fields,
                unique_fields=unique_fields,
            )
            logger.info(f"{len(characters)} Characters created/updated")

        lskills = gamedbparser.parse_leader_skills(masterdb_conn)
        if len(lskills) > 0:
            updatable_fields = set(lskills[0].__dict__).difference(non_updatable_fields)
            LeaderSkill.objects.bulk_create(
                lskills,
                update_conflicts=True,
                update_fields=updatable_fields,
                unique_fields=unique_fields,
            )
            logger.info(f"{len(lskills)} Leader skills created/updated")

        durs = gamedbparser.parse_skill_duration(masterdb_conn)
        if len(durs) > 0:
            updatable_fields = set(durs[0].__dict__).difference(non_updatable_fields)
            SkillDuration.objects.bulk_create(
                durs,
                update_conflicts=True,
                update_fields=updatable_fields,
                unique_fields=unique_fields,
            )
        probs = gamedbparser.parse_skill_probability(masterdb_conn)
        if len(probs) > 0:
            updatable_fields = set(probs[0].__dict__).difference(non_updatable_fields)
            SkillProbability.objects.bulk_create(
                probs,
                update_conflicts=True,
                update_fields=updatable_fields,
                unique_fields=unique_fields,
            )

        skills = gamedbparser.parse_skills(masterdb_conn)
        if len(skills) > 0:
            updatable_fields = set(skills[0].__dict__).difference(non_updatable_fields)
            Skill.objects.bulk_create(
                skills,
                update_conflicts=True,
                update_fields=updatable_fields,
                unique_fields=unique_fields,
            )
            logger.info(f"{len(skills)} Skills created/updated")

        cards = gamedbparser.parse_cards(masterdb_conn)
        if len(cards) > 0:
            updatable_fields = set(cards[0].__dict__).difference(non_updatable_fields)
            Card.objects.bulk_create(
                cards,
                update_conflicts=True,
                update_fields=updatable_fields,
                unique_fields=unique_fields,
            )
            if not options["nodl"]:
                self.update_card_icons(cards)
        masterdb_conn.close()

    def update_card_icons(self, cards: list[Card]):
        for card in cards:
            path = paths.get_card_icon_path(card.id)
            if path.exists():
                continue
            icon = request_card_icon(card.id)
            with files.get_writer(path, "wb") as f:
                f.write(icon)
