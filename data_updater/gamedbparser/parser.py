import logging
import sqlite3

from django.db import models

from charas.models import Character
from cards.models import LeaderSkill, SkillDuration, SkillProbability, Skill, Card

logger = logging.getLogger(__name__)


def parse_characters(conn: sqlite3.Connection) -> list[Character]:
    cur = conn.cursor()
    rows = cur.execute(
        "SELECT chara_id, name, name_kana FROM chara_data WHERE base_card_id != 0"
    ).fetchall()
    logger.info(f"Found {len(rows)} characters in db")
    cur.close()
    charas = []
    for row in rows:
        charas.append(Character(id=row[0], name=row[1], name_kana=row[2]))
    return charas


def parse_leader_skills(conn: sqlite3.Connection) -> list[LeaderSkill]:
    cur = conn.cursor()
    rows = cur.execute("SELECT id, name, explain FROM leader_skill_data").fetchall()
    logger.info(f"Found {len(rows)} leader skills in db")
    cur.close()
    lskills = []
    for row in rows:
        lskills.append(LeaderSkill(id=row[0], name=row[1], desc=row[2]))
    return lskills


def parse_skill_duration(conn: sqlite3.Connection) -> list[SkillDuration]:
    cur = conn.cursor()
    rows = cur.execute(
        "SELECT available_time_type, available_time_min, available_time_max, explain FROM available_time_type"
    ).fetchall()
    cur.close()
    durs = []
    for row in rows:
        durs.append(
            SkillDuration(
                id=row[0], min_duration=row[1], max_duration=row[2], desc=row[3]
            )
        )
    return durs


def parse_skill_probability(conn: sqlite3.Connection) -> list[SkillDuration]:
    cur = conn.cursor()
    rows = cur.execute(
        "SELECT probability_type, probability_min, probability_max, explain FROM probability_type"
    ).fetchall()
    cur.close()
    probs = []
    for row in rows:
        probs.append(
            SkillProbability(
                id=row[0], min_probability=row[1], max_probability=row[2], desc=row[3]
            )
        )
    return probs


def parse_skills(conn: sqlite3.Connection) -> list[Skill]:
    cur = conn.cursor()
    rows = cur.execute(
        """
        SELECT id, skill_name, explain, skill_type, condition, probability_type, available_time_type
        FROM skill_data
    """
    ).fetchall()
    logger.info(f"Found {len(rows)} skills in db")
    cur.close()

    probs_cache = {}
    durs_cache = {}
    skills = []
    for row in rows:
        prob_id = row[5]
        if prob_id not in probs_cache:
            try:
                probs_cache[prob_id] = SkillProbability.objects.get(id=prob_id)
            except SkillProbability.DoesNotExist as e:
                logger.error(
                    f"Invalid skill probability with id={prob_id} for skill with id={row[0]}. Skipping..."
                )
                continue
        probability = probs_cache[prob_id]

        dur_id = row[6]
        if dur_id not in durs_cache:
            try:
                durs_cache[dur_id] = SkillDuration.objects.get(id=dur_id)
            except SkillDuration.DoesNotExist as e:
                logger.error(
                    f"Invalid skill duration with id={dur_id} for skill with id={row[0]}. Skipping..."
                )
                continue
        duration = durs_cache[dur_id]

        skills.append(
            Skill(
                id=row[0],
                name=row[1],
                desc=row[2],
                skill_type=row[3],
                timer=row[4],
                probability=probability,
                duration=duration,
            )
        )
    return skills


def _get_obj(
    cls: type[models.Model], id: int, cache: dict[int, models.Model] | None = None
) -> models.Model | None:
    if cache is not None and id in cache:
        return cache[id]
    else:
        obj = None
        try:
            obj = cls.objects.get(id=id)
        except cls.DoesNotExist:
            # just return None if it does not exist
            pass
        if cache is not None:
            cache[id] = obj
        return obj


def parse_cards(conn: sqlite3.Connection) -> list[Card]:
    cur = conn.cursor()
    rows = cur.execute(
        """SELECT id, name, chara_id, rarity, attribute,
        skill_id, leader_skill_id,
        hp_min, hp_max, bonus_hp,
        visual_min, visual_max, bonus_visual,
        vocal_min, vocal_max, bonus_vocal,
        dance_min, dance_max, bonus_dance FROM card_data"""
    ).fetchall()
    cur.close()

    chara_cache = {}
    leader_skill_cache = {}
    cards = []
    for row in rows:
        # skip non-game cards
        if str(row[0])[0] not in ["1", "2", "3"]:
            continue
        character = _get_obj(Character, row[2], chara_cache)
        if character is None:
            logger.error(
                f"Invalid character with id={row[2]} for card with id={row[0]}. Skipping..."
            )
            continue
        lskill = _get_obj(LeaderSkill, row[6], leader_skill_cache)
        if lskill is None and row[6] != 0:
            logger.error(
                f"Invalid leader skill with id={row[6]} for card with id={row[0]}. Skipping..."
            )
            continue
        skill = _get_obj(Skill, row[5])
        if skill is None and row[5] != 0:
            logger.error(
                f"Invalid skill with id={row[5]} for card with id={row[0]}. Skipping..."
            )
            continue
        cards.append(
            Card(
                id=row[0],
                name=row[1],
                character=character,
                rarity=row[3],
                attribute=row[4],
                skill=skill,
                leader_skill=lskill,
                hp_min=row[7],
                hp_max=row[8],
                hp_bonus=row[9],
                vi_min=row[10],
                vi_max=row[11],
                vi_bonus=row[12],
                vo_min=row[13],
                vo_max=row[14],
                vo_bonus=row[15],
                da_min=row[16],
                da_max=row[17],
                da_bonus=row[18],
            )
        )
    return cards
