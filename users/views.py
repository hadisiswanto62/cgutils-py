from django.db.models import QuerySet
from django.shortcuts import redirect

from .models import OwnedCard, UserData
from cards.models import Card
from cards.views import CardListView, CardFilter

class UserOwnedCardListView(CardListView):
    def get_queryset(self) -> QuerySet[Card]:
        # TODO: return QuerySet[OwnedCard]
        owned = OwnedCard.objects.filter(user_data__user=self.request.user)
        cards = Card.objects.filter(ownedcard__in=owned).distinct()
        return CardFilter(self.request.GET, queryset=cards).qs
    
    def post(self, request, *args, **kwargs):
        to_create = []
        for key in request.POST:
            if key.startswith("card-"):
                card_id = int(key.lstrip("card-"))
                card = Card.objects.filter(id=card_id).first()
                user_data = UserData.objects.get(user=self.request.user)
                to_create.append(OwnedCard(user_data=user_data, card=card, level=card.get_max_level(), skill_level=10))
        OwnedCard.objects.bulk_create(to_create)
        return redirect("add_ownedcard")