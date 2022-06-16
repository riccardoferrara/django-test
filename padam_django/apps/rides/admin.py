from django.contrib import admin
from .models import BusStop, BusShift

class BusStopInline(admin.TabularInline):
    model = BusStop
    extra = 10
    ordering = ('time', )

class BusShiftAdmin(admin.ModelAdmin):
    inlines = [BusStopInline]
    list_display = ('driver', 'bus')

class BusStopAdmin(admin.ModelAdmin):
    list_display = ('place', 'time', 'busshift')
    list_filter = ['busshift', 'time']

admin.site.register(BusShift, BusShiftAdmin)

admin.site.register(BusStop, BusStopAdmin)
