from rest_framework import serializers

from cultivator.models import Cultivator

class CultivatorSerializers(serializers.ModelSerializer):
  class Meta:
    model = Cultivator
    fields = ['id','first_name', 'last_name', 'username', 'email', 'password']