from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from cards.models import Card


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class OwnedCard(models.Model):
    user_data = models.ForeignKey(UserData, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    level = models.IntegerField()
    skill_level = models.IntegerField()

class Team(models.Model):
    name = models.TextField()
    cards = models.ManyToManyField(to=OwnedCard)

    def clean(self):
        if self.cards.count() > 5:
            raise ValidationError("Team has too many cards")
        super().clean()

    def save(self, *args, **kwargs):
        if self.id is not None:
            self.full_clean()
        super().save(*args, **kwargs)