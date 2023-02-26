from django.utils.translation import gettext_lazy as _
from django.db import models


class Rarity(models.IntegerChoices):
    N = 1, _("N")
    NPlus = 2, _("N+")
    R = 3, _("R")
    RPlus = 4, _("R+")
    SR = 5, _("SR")
    SRPlus = 6, _("SR+")
    SSR = 7, _("SSR")
    SSRPlus = 8, _("SSR+")


class CardAttribute(models.IntegerChoices):
    Cute = 1
    Cool = 2
    Passion = 3
