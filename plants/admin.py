from django.contrib import admin
from plants.models import Plant

class Plants(admin.ModelAdmin):
  list_display = ('id', 'code', 'name', 'temperature', 'watering_week', 'description')
  list_display_links = ('id', 'code', 'name')
  search_fields = ('id', 'code', 'name',)
  list_filter = ('id', 'code', 'name', 'temperature',)
  list_per_page = 10
  ordering = (['code'])

admin.site.register(Plant, Plants)