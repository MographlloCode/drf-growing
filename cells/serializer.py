from rest_framework import serializers

from cells.models import Cell
from plants.serializer import PlantSerializers

from cells.validators import *

class CellSerializers(serializers.ModelSerializer):
  class Meta:
    model = Cell
    fields = ['code', 'plant']

  def validate(self, data):
    if not valid_code(data['code']):
      raise serializers.ValidationError({'code':"The code must have 6 digits."})
    return data