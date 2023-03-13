from django.test import TestCase
from django.core.exceptions import ValidationError
from cards.tests import _create_card, _create_chara
from model_bakery import baker

from .models import UserData, OwnedCard, Team

class TeamTest(TestCase):
    def test_team_maxcard(self):
        u = baker.make("auth.User")
        ud = UserData.objects.get(user=u)
        ocs = [baker.make("users.OwnedCard", user_data=ud)
                for _ in range(6)]
        team = Team.objects.create(name="test")
        for oc in ocs[:5]:
            team.cards.add(oc)
        team.save()

        team.cards.add(ocs[-1])
        with self.assertRaises(ValidationError):
            team.save()