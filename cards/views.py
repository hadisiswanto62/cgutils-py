from django.http.request import HttpRequest
from django.views.generic.list import ListView
from django.db.models import QuerySet
from django_filters import FilterSet
from .models import Card, Rarity

class CardFilter(FilterSet):
    DEFAULT_FILTER = {
        "rarity": Rarity.SSRPlus.value,
    }
    class Meta:
        model = Card
        fields = ["rarity"]

    def __init__(self, data=None, *args, **kwargs):
        if data is not None:
            data = data.copy()
            for name in self.base_filters.keys():
                if name not in data and name in self.DEFAULT_FILTER:
                    data[name] = self.DEFAULT_FILTER[name]

        super().__init__(data, *args, **kwargs)


class CardListView(ListView):
    model = Card
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = CardFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self) -> QuerySet[Card]:
        queryset = super().get_queryset()
        return CardFilter(self.request.GET, queryset=queryset).qs