from django.shortcuts import render

from rest_framework import viewsets

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.decorators import action

from rest_framework.generics import RetrieveUpdateDestroyAPIView

from api.models import AlbumModel,TrackModel,User,review_model

from api.serializers import AlbumSerializer,TrackSerializer,UserSerializer,Review_Serializer

from rest_framework import authentication,permissions

from api.permissions import OwnerOnly




class AlbumViewsetView(viewsets.ModelViewSet):

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
        

class Track_mixin(RetrieveUpdateDestroyAPIView):

    serializer_class=TrackSerializer

    queryset=TrackModel.objects.all()



class signUp_view(viewsets.ViewSet):

    def create(self,request,*args,**kwargs):

        serializer=UserSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(data=serializer.data)

        else:

            return Response(data=serializer.errors)


class Review_addView(APIView):

    permission_classes=[OwnerOnly]

    authentication_classes=[authentication.TokenAuthentication]

    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        album_instance=AlbumModel.objects.get(id=id)

        serializer=Review_Serializer(data=request.data)

        if serializer.is_valid():

            serializer.save(user=request.user,album=album_instance)

            return Response(data=serializer.data)
        
        else:

            return Response(data=serializer.errors)
        

class review_Mixin(RetrieveUpdateDestroyAPIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[OwnerOnly]

    serializer_class=Review_Serializer

    queryset=review_model.objects.all()