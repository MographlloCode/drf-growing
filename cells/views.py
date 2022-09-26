from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from cells.models import Cell
from cells.serializer import CellSerializers

class CellViewset(viewsets.ModelViewSet):
  ''' Exibindo dados do cultivador '''
  queryset = Cell.objects.all()
  serializer_class = CellSerializers
  filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
  ordering_fields = ['code']
  search_fields = ['code']