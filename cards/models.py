from django.db import models

from .enum_models import Rarity, CardAttribute
from charas.models import Character


class LeaderSkill(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    desc = models.TextField()


class SkillDuration(models.Model):
    id = models.IntegerField(primary_key=True)
    min_duration = models.IntegerField()
    max_duration = models.IntegerField()
    desc = models.TextField()


class SkillProbability(models.Model):
    id = models.IntegerField(primary_key=True)
    min_probability = models.IntegerField()
    max_probability = models.IntegerField()
    desc = models.TextField()


class Skill(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    desc = models.TextField()
    skill_type = models.IntegerField()
    timer = models.IntegerField()
    probability = models.ForeignKey(SkillProbability, on_delete=models.CASCADE)
    duration = models.ForeignKey(SkillDuration, on_delete=models.CASCADE)


class Card(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    rarity = models.IntegerField(choices=Rarity.choices)
    attribute = models.IntegerField(choices=CardAttribute.choices)
    skill = models.ForeignKey(Skill, null=True, on_delete=models.CASCADE)
    leader_skill = models.ForeignKey(LeaderSkill, null=True, on_delete=models.CASCADE)

    hp_min = models.IntegerField()
    hp_max = models.IntegerField()
    hp_bonus = models.IntegerField()
    vi_min = models.IntegerField()
    vi_max = models.IntegerField()
    vi_bonus = models.IntegerField()
    vo_min = models.IntegerField()
    vo_max = models.IntegerField()
    vo_bonus = models.IntegerField()
    da_min = models.IntegerField()
    da_max = models.IntegerField()
    da_bonus = models.IntegerField()

    @property
    def is_evolved(self):
        return self.rarity % 2 == 0
