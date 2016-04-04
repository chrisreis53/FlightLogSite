from django.contrib import admin

# Register your models here.
from .models import Pilot
from .models import Mission
from .models import Airport
from .models import Aircraft
from .models import Flightdata

admin.site.register(Pilot)
admin.site.register(Mission)
admin.site.register(Airport)
admin.site.register(Aircraft)
admin.site.register(Flightdata)
