from django.core.management.base import BaseCommand, CommandError
import logging
import sqlite3

from data_updater.utils import paths
from data_updater import gamedbparser, updater
from charas.models import Character

class Command(BaseCommand):
    def handle(self, *args, **options):
        # updater.update_manifest()
        # updater.update_master()

        masterdb_conn = sqlite3.connect(paths.MASTERDB_PATH)
        masterdb_conn.row_factory = sqlite3.Row
        characters = gamedbparser.parse_characters(masterdb_conn)
        Character.objects.bulk_create(characters)
        masterdb_conn.close()