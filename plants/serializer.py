from unicodedata import category
from rest_framework import serializers

from plants.models import Plant
from plants.validators import *

class PlantSerializers(serializers.ModelSerializer):
  class Meta:
    model = Plant
    fields = ['code', 'name', 'temperature', 'watering_week', 'description']
  
  def validate(self, data):
    if not valid_code(data['code']):
      raise serializers.ValidationError({'code':"The code must have 6 digits."})
    if not valid_name(data['name']):
      raise serializers.ValidationError({'name':"Don't include numbers at the name field."})
    return data