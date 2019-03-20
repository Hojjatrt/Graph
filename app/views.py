from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print('index')
    return render(request, 'app/index.html', {})


def game(request):
    print('game')
    return render(request, 'app/graph.html', {})
