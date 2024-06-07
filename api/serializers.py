from rest_framework import serializers

from api.models import AlbumModel,TrackModel



class AlbumSerializer(serializers.ModelSerializer):

    track_count=serializers.CharField(read_only=True)

    class Meta:

        model=AlbumModel

        fields="__all__"

        read_only_fields=["id","created_date","updated_date","is_active"]


class TrackSerializer(serializers.ModelSerializer):

    album=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=TrackModel

        fields="__all__"

        read_only_fields=["id","album","created_date","updated_date","is_active"]
        