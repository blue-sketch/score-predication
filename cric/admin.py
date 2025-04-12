from django.contrib import admin
from .models import Cricket,Feedback,Team,Player,Format,PlayerStats,ReportCard

#register model here 
admin.site.register(Cricket)
admin.site.register(Feedback)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Format)
admin.site.register(PlayerStats)
admin.site.register(ReportCard)
