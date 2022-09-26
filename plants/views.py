from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from plants.models import Plant
from plants.serializer import PlantSerializers

class PlantsViewset(viewsets.ModelViewSet):
  ''' Exibindo todas as Plantas '''
  queryset = Plant.objects.all()
  serializer_class = PlantSerializers
  filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
  ordering_fields = ['code']
  search_fields = ['code', 'name']