from django.contrib import admin
from cells.models import Cell

class Cells(admin.ModelAdmin):
  list_display = ('id', 'code', 'plant',)
  list_display_links = ('id', 'code', 'plant',)
  search_fields = ('id', 'code', 'plant',)
  list_filter = ('id', 'code', 'plant',)
  list_per_page = 10
  ordering = (['code'])

admin.site.register(Cell, Cells)