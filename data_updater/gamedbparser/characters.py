from charas.models import Character
import sqlite3

def parse_characters(conn: sqlite3.Connection) -> list[Character]:
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM chara_data WHERE base_card_id != 0").fetchall()
    cur.close()
    charas = []
    for row in rows:
        charas.append(Character(id=row["chara_id"], name=row["name"], name_kana=row["name_kana"]))
    return charas