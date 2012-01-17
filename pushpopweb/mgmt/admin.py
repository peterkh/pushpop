from mgmt.models import Dashboard, DashboardEntry
from django.contrib import admin

class DashboardAdmin(admin.ModelAdmin):
    list_display = ['name', 'public']

admin.site.register(Dashboard, DashboardAdmin)
admin.site.register(DashboardEntry)

