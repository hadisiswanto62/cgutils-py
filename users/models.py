from django.db import models
from django.contrib.auth.models import User

from cards.models import Card


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class OwnedCard(models.Model):
    user_data = models.ForeignKey(UserData, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    level = models.IntegerField()
    skill_level = models.IntegerField()
