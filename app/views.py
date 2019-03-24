import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import *


def index(request):
    print('index')
    return render(request, 'app/index.html', {})


def game(request):
    print('game')
    return render(request, 'app/graph.html', {})


def data(request):
    graph = Graph.objects.first()
    nodes = []
    for i in graph.nodes.all():
        nodes.append({'name': i.name, 'num': i.num, 'x': i.x, 'y': i.y})
    links = []
    for i in graph.links.all():
        links.append({'id': i.id, 'num': i.num, 'source': i.source.num, 'target': i.target.num, 'weight': i.weight})
    return JsonResponse({'nodes': nodes, 'links': links, 'g_id': graph.id})


@method_decorator(csrf_exempt)
def save_movement(request):
    if request.is_ajax():
        if request.method == 'POST' and request.user.is_authenticated:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            PlayerLinkAdvanced.objects.create(link_id=body['id'], graph_id=body['graph'],
                                              weight=body['weight'], player_id=request.user.id)
            return JsonResponse({'status': 'OK'})
    return JsonResponse({'status': 'NOK'})
