from django.contrib import admin
from .models import Rider

class reqAdmin(admin.ModelAdmin):
    list_display = ('from_location','to_location','date','travel_medium','assets_quantity')
    list_filter = ('travel_medium',)
    list_per_page = 5
admin.site.register(Rider,reqAdmin)
# Register your models here.
