from django.contrib import admin
from .models import Requester

class reqAdmin(admin.ModelAdmin):
    list_display = ('from_location','to_location','date','assets','asset_type','sensitivities','recipient')
    list_filter = ('asset_type',)
    list_per_page = 5
admin.site.register(Requester,reqAdmin)
# Register your models here.
