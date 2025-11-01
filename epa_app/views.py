from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import SiteMetaData, SiteAqiData
from datetime import time, datetime, date, timedelta
# Create your views here.
from rest_framework import routers, serializers, viewsets, generics
from rest_framework.exceptions import ValidationError

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
    
class SiteAqiDataViewSet(viewsets.ModelViewSet):
    serializer_class = SiteAqiDataSerializer

    def get_queryset(self):
        queryset = SiteAqiData.objects.all()

        # Filter by site_id from nested router
        site_id = self.kwargs.get('sitemetadata_pk')
        queryset = queryset.filter(site_id=site_id)  

        # Get query parameters
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        pollutant = self.request.query_params.get('pollutant')

        # Handle start date
        if start_date:
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            except ValueError:
                raise ValidationError("start_date must be YYYY-MM-DD")
        else:
            # Pick earliest date for this site
            earliest = queryset.order_by('date').first()
            if earliest:
                start_date = earliest.date

        # Handle end date
        if end_date:
            try:
                end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
            except ValueError:
                raise ValidationError("end_date must be YYYY-MM-DD")

        # Apply filters
        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            queryset = queryset.filter(date__lte=end_date)
        if pollutant:
            queryset = queryset.filter(pollutant=pollutant)

        return queryset