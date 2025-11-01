from rest_framework import serializers
from .models import SiteAqiData, SiteMetaData  # replace with your model

class SiteAqiDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteAqiData
        fields = '__all__'  # or list specific fields

class SiteMetaDataSerializer(serializers.ModelSerializer):
  class Meta:
    model = SiteMetaData
    fields = '__all__'
