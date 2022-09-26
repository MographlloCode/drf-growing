from rest_framework import viewsets, generics

from cultivator.models import Cultivator
from cultivator.serializer import CultivatorSerializers

class CultivatorViewset(viewsets.ModelViewSet):
  ''' Exibindo dados do cultivador '''
  queryset = Cultivator.objects.all()
  serializer_class = CultivatorSerializers
  
class ListCultivatorData(generics.ListAPIView):
  ''' Exibindo dados do cultivador '''
  queryset = Cultivator.objects.all()
  serializer_class = CultivatorSerializers
  
# class ListCultivatorPlants(generics.ListAPIView):
#   ''' Exibindo dados do cultivador '''
#   def get_queryset(self):
#     queryset = Cultivator.objects.filter(cultivator_id=self.kwargs['pk'])
#     return queryset
#   serializer_class = CultivatorSerializers
  
# class ListCultivatorPlantData(generics.ListAPIView):
#   ''' Exibindo dados do cultivador '''
#   def get_queryset(self):
#     queryset = Cultivator.objects.filter(cultivator_id=self.kwargs['pk'])
#     return queryset
#   serializer_class = CultivatorSerializers
  
# class ListCultivatorCells(generics.ListAPIView):
#   ''' Exibindo dados do cultivador '''
#   def get_queryset(self):
#     queryset = Cultivator.objects.filter(cultivator_id=self.kwargs['pk'])
#     return queryset
#   serializer_class = CultivatorSerializers
  
# class ListCultivatorCellData(generics.ListAPIView):
  ''' Exibindo dados do cultivador '''
  def get_queryset(self):
    queryset = Cultivator.objects.filter(cultivator_id=self.kwargs['pk'])
    return queryset
  serializer_class = CultivatorSerializers