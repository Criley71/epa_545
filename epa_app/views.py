from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import SiteMetaData, SiteAqiData
from datetime import time, datetime, date, timedelta
# Create your views here.
from rest_framework import routers, serializers, viewsets, generics

class SiteMetaDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SiteMetaData
        fields = '__all__'

class SiteAqiDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SiteAqiData
        fields = ['site_id', 'state', 'county', 'pollutant', 'value', 'units', 'date']

# ViewSets define the view behavior.
class SiteMetaDataViewSet(viewsets.ModelViewSet):
    queryset = SiteMetaData.objects.all()
    serializer_class = SiteMetaDataSerializer

class SiteAqiDataViewSet(viewsets.ModelViewSet):
    queryset = SiteAqiData.objects.all()
    serializer_class = SiteAqiDataSerializer


class SearchQuerysetMixin():
    def get_queryset(self):
        queryset = self.model.objects.all()
        valid_fields = self.model._meta.fields
        filters = {}
        for param in self.request.query_params.lists():
            if param[0] == 'start_date':
                parsed = datetime.strptime(param[1][0], "%Y-%m-%d").date()
                filters["date__gte"] = parsed
            elif param[0] == 'end_date':
                parsed = datetime.strptime(param[1][0], "%Y-%m-%d").date()
                filters["date__lte"] = parsed
            else:
                filters[param[0]] = param[1][0]
        print(filters)
        queryset = queryset.filter(**filters)
        return queryset

class SiteAqiDataList(SearchQuerysetMixin, generics.ListAPIView):
    serializer_class = SiteAqiDataSerializer
    model = SiteAqiData
