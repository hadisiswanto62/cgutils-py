from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from cards.models import Card

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cards = models.ManyToManyField(to=Card)

class Team(models.Model):
    user_data = models.ForeignKey(UserData, on_delete=models.CASCADE)
    name = models.TextField()
    leader = models.ForeignKey(to=Card, null=True, on_delete=models.SET_NULL, related_name="leader")
    cards = models.ManyToManyField(to=Card, related_name="nonleaders")

    def clean(self):
        count = self.cards.count()
        if self.leader is not None:
            count += 1
        if count > 5:
            raise ValidationError("Team has too many cards")
        super().clean()

    def save(self, *args, **kwargs):
        if self.id is not None:
            self.full_clean()
        super().save(*args, **kwargs)