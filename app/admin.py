from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Node)
admin.site.register(Link)
admin.site.register(Graph)
admin.site.register(PlayerLink)
admin.site.register(PlayerLinkAdvanced)
admin.site.register(Score)
admin.site.register(ScoreAdvances)
