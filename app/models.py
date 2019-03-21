from django.contrib.auth.models import User
from django.db import models
from .fields import *
from django.utils.translation import ugettext_lazy as _


class Node(models.Model):
    num = models.PositiveSmallIntegerField(_('Number'), unique=True)
    x = models.SmallIntegerField(_('X'))
    y = models.SmallIntegerField(_('Y'))
    name = models.CharField(_('Name'), max_length=10, default='node')

    def __str__(self):
        return self.name


class Link(models.Model):
    num = models.PositiveSmallIntegerField(_('Number'), unique=True)
    source = models.ForeignKey(Node, verbose_name=_('Source'), related_name="sources", on_delete=models.CASCADE)
    target = models.ForeignKey(Node, verbose_name=_('Target'), related_name="targets", on_delete=models.CASCADE)
    weight = models.SmallIntegerField(_('Weight'))

    def __str__(self):
        return str(self.num) + " - " + str(self.weight)


class Graph(models.Model):
    level = models.PositiveSmallIntegerField(_('Level'))
    nodes = models.ManyToManyField(Node, verbose_name=_('Nodes'))
    links = models.ManyToManyField(Link, verbose_name=_('Links'))
    name = models.CharField(_('Name'), max_length=10, default='node')

    def __str__(self):
        return self.name
