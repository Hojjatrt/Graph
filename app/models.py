from django.contrib.auth.models import User
from django.db import models
from .fields import *
from .choices import *
from django.utils.translation import ugettext_lazy as _
# Create your models here.
#
#
# class Graph(models.Model):
#     nodes = models.CharField(_('Part1'), default="12", max_length=2)
#     alpha = models.CharField(_('Alpha'), max_length=10, choices=ALPHA_CHOICES)
#     part2 = models.CharField(_('Part2'), default="123", max_length=3)
#     country = models.CharField(_('Country'), default="ایران", max_length=20)
#     region = models.CharField(_('Region'), default="95", max_length=2)
#     image = models.ImageField(_('Image'), upload_to='app/%Y/%m/%d', blank=True, null=True)
#
#     def save(self, force_insert=False, force_update=False, using=None,
#              update_fields=None):
#
#         super(Graph, self).save(force_insert, force_update)
#
#     def __str__(self):
#         return self.part1 + self.alpha + self.part2
#
#     class Meta:
#         verbose_name = _("Plaque")
#         verbose_name_plural = _("Plaques")
