from django.test import TestCase
from charas.models import Character
from .models import *


def _create_card(id: int, chara_id: int, **kwargs):
    default = {
        "name": f"card_name{id}",
        "character": Character.objects.get(id=chara_id),
        "rarity": 8,
        "attribute": 1,
        "hp_min": 0,
        "hp_max": 0,
        "hp_bonus": 0,
        "vi_min": 0,
        "vi_max": 0,
        "vi_bonus": 0,
        "vo_min": 0,
        "vo_max": 0,
        "vo_bonus": 0,
        "da_min": 0,
        "da_max": 0,
        "da_bonus": 0,
    }
    default.update(kwargs)
    return Card.objects.create(**default)


def _create_chara(id: int, **kwargs):
    default = {"name": f"chara{id}", "name_kana": f"chara_kana{id}"}
    default.update(kwargs)
    return Character.objects.create(**default)


# Create your tests here.
class CardTestCase(TestCase):
    def setUp(self):
        _create_chara(1)

    def test_is_evolved(self):
        card = _create_card(100, 1, rarity=1)
        self.assertEqual(card.is_evolved, False)
        card = _create_card(101, 1, rarity=2)
        self.assertEqual(card.is_evolved, True)

    def test_max_level(self):
        card = _create_card(200, 1, rarity=8)
        self.assertEqual(card.get_max_level(), 90)
