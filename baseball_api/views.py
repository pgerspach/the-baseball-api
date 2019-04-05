from .models import Player, Batting, Pitching
from django.template import loader
from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic
from django.forms.models import model_to_dict
import logging
logger = logging.getLogger(__name__)
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'baseball_api/index.html'

# class PlayerView(generic.DetailView):
#     template_name = 'baseball_api/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['latest_articles'] = Article.objects.all()[:5]
#         return context
def player(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    player = model_to_dict(player)
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    print(player)
    return JsonResponse(player, safe=False)


def batting(request, player_id):
    batting = list(Batting.objects.filter(player=player_id).values())
    # batting = batting.map(lambda x :model_to_dict(x))
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    for x in batting:
        x["avg"]=float('%.3f'%(x["h"]/x["ab"]))

    return JsonResponse(batting, safe=False)

def pitching(request, player_id):
    pitching = list(Pitching.objects.filter(player=player_id).values())
    # batting = batting.map(lambda x :model_to_dict(x))
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return JsonResponse(pitching, safe=False)