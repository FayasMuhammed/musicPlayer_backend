from rest_framework import serializers

from api.models import AlbumModel,TrackModel,User,review_model



class Review_Serializer(serializers.ModelSerializer):

    album=serializers.StringRelatedField(read_only=True)

    user=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=review_model

        fields="__all__"

        read_only_fields=["id","user","album","created_date","updated_date","is_active"]
        



class TrackSerializer(serializers.ModelSerializer):

    album=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=TrackModel

        fields="__all__"

        read_only_fields=["id","album","created_date","updated_date","is_active"]



class AlbumSerializer(serializers.ModelSerializer):

    track_count=serializers.CharField(read_only=True)

    track_list=TrackSerializer(read_only=True,many=True)

    review_list=Review_Serializer(read_only=True,many=True)

    class Meta:

        model=AlbumModel

        fields=["id","title","year","director","language","created_date","updated_date","is_active","track_count","track_list","review_list"]

        read_only_fields=["id","created_date","updated_date","is_active"]





class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=["id","username","password","email"]

        read_only_fields=["id"]

    def create(self,validated_data):

        return User.objects.create_user(**validated_data)
    

