from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from rest_framework.decorators import action

from api.models import AlbumModel

from api.serializers import AlbumSerializer,TrackSerializer

from rest_framework import authentication,permissions




class AlbumViewsetView(ModelViewSet):

    serializer_class=AlbumSerializer

    queryset=AlbumModel.objects.all()

    @action(methods=["post"],detail=True)
    def add_track(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        album_instance=AlbumModel.objects.get(id=id)

        serializer=TrackSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(album=album_instance)

            return Response(data=serializer.data)
        
        else:

            return Response(data=serializer.errors)



