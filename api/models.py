from django.db import models



class AlbumModel(models.Model):

    title=models.CharField(max_length=200)

    year=models.CharField(max_length=200)

    director=models.CharField(max_length=200)

    language=models.CharField(max_length=200)

    created_date=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)




class TrackModel(models.Model):

    title=models.CharField(max_length=200)

    singers=models.CharField(max_length=200)

    genre=models.CharField(max_length=200)

    duration=models.CharField(max_length=200)

    track_number=models.CharField(max_length=100)

    album=models.ForeignKey(AlbumModel,on_delete=models.CASCADE)



