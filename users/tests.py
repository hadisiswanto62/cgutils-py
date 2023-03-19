from django.test import TestCase
from django.core.exceptions import ValidationError
from cards.tests import _create_card, _create_chara
from model_bakery import baker

from .models import UserData, Team

class TeamTest(TestCase):
    def test_team_maxcard(self):
        u = baker.make("auth.User")
        ud = UserData.objects.get(user=u)
        cards = [baker.make("cards.Card") for _ in range(6)]
        team = Team.objects.create(name="test", user_data=ud, leader=cards[0])
        for card in cards[1:5]:
            team.cards.add(card)
        team.save()

        team.cards.add(cards[-1])
        with self.assertRaises(ValidationError):
            team.save()