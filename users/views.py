from django.db.models import QuerySet
from django.shortcuts import redirect

from .models import UserData
from cards.models import Card
from cards.views import CardListView, CardFilter

class UserOwnedCardListView(CardListView):
    def get_queryset(self) -> QuerySet[Card]:
        ud = UserData.objects.get(user=self.request.user.id)
        cards = ud.cards.all()
        return CardFilter(self.request.GET, queryset=cards).qs
    
    def post(self, request, *args, **kwargs):
        to_create = []
        user_data = UserData.objects.get(user=self.request.user)
        for key in request.POST:
            if key.startswith("card-"):
                card_id = int(key.lstrip("card-"))
                card = Card.objects.filter(id=card_id).first()
                user_data.cards.add(card)
        user_data.save()
        return redirect("add_ownedcard")