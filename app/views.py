from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
        links.append({'num': i.num, 'source': i.source.num, 'target': i.target.num, 'weight': i.weight})
    return JsonResponse({'nodes': nodes, 'links': links})
