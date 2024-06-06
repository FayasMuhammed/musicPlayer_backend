from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from api.models import AlbumModel

from api.serializers import AlbumSerializer

from rest_framework import authentication,permissions




class AlbumViewsetView(ModelViewSet):

    serializer_class=AlbumSerializer

    queryset=AlbumModel.objects.all()

