from data_updater import network, utils
from data_updater.utils import paths

import sqlite3
import logging

logger = logging.getLogger(__name__)
def update_manifest():
    version = network.request_truth_version()
    logger.info(f"Getting manifest v{version}...")
    man_bytes = network.request_manifest(version)
    with utils.get_writer(paths.MANIFEST_PATH, "wb") as f:
        f.write(utils.decompress(man_bytes))
    logger.info("Manifest updated.")

def update_master():
    con = sqlite3.connect(paths.MANIFEST_PATH)
    cur = con.cursor()
    cur.execute("""
    SELECT * FROM manifests WHERE name='master.mdb'
    """)
    row = cur.fetchone()
    hash = row[1]
    logger.info(f"Getting master with hash '{hash}'...")
    # master_bytes = network.request_db(hash)
    # with utils.get_writer(paths.MASTERDB_PATH, "wb") as f:
    #     f.write(utils.decompress(master_bytes))
    logger.info("Game master DB updated.")
    cur.close()
    con.close()
