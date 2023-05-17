from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(Malle)
admin.site.register(Femalle)

admin.site.register(PoidFemalle)
admin.site.register(PoidMalle)

from django.contrib import admin
from .models import*
admin.site.register(PoidLapinProduction)

admin.site.register(LapinProduction)
admin.site.register(GroupeProduction)
admin.site.register(Accouplement)
admin.site.register(VaccinLapin)

