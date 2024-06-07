from django.db import models

from django.db.models import Sum



class AlbumModel(models.Model):

    title=models.CharField(max_length=200)

    year=models.CharField(max_length=200)

    director=models.CharField(max_length=200)

    language=models.CharField(max_length=200)

    created_date=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)

    @property
    def track_count(self):
        return TrackModel.objects.filter(album=self).count()


    def __str__(self) -> str:
        return self.title




class TrackModel(models.Model):

    title=models.CharField(max_length=200)

    singers=models.CharField(max_length=200)

    genre=models.CharField(max_length=200)

    duration=models.CharField(max_length=200)

    track_number=models.CharField(max_length=100)

    album=models.ForeignKey(AlbumModel,on_delete=models.CASCADE)

    created_date=models.DateTimeField(auto_now_add=True,null=True)

    updated_date=models.DateTimeField(auto_now=True,null=True)

    is_active=models.BooleanField(default=True,null=True)

    def __str__(self):
        return self.title



