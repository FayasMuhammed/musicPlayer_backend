from rest_framework import serializers

from api.models import AlbumModel



class AlbumSerializer(serializers.ModelSerializer):

    class Meta:

        model=AlbumModel

        fields="__all__"

        read_only_fields=["id","created_date","updated_date","is_active"]
        