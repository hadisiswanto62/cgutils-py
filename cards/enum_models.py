from django.db import models


class Rarity(models.IntegerChoices):
    N = 1
    NPlus = 2
    R = 3
    RPlus = 4
    SR = 5
    SRPlus = 6
    SSR = 7
    SSRPlus = 8


class CardAttribute(models.IntegerChoices):
    Cute = 1
    Cool = 2
    Passion = 3
