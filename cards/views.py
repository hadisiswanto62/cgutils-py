from django.views.generic.list import ListView
from django.db.models import QuerySet
from django_filters import FilterSet
from .models import Card


class CardFilter(FilterSet):
    class Meta:
        model = Card
        fields = ["attribute"]


class CardListView(ListView):
    model = Card
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = CardFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self) -> QuerySet[Card]:
        queryset = super().get_queryset()
        return CardFilter(self.request.GET, queryset=queryset).qs
