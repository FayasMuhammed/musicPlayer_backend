from django.urls import path

from api.views import AlbumViewsetView

from rest_framework.routers import DefaultRouter


router=DefaultRouter()

router.register("album",AlbumViewsetView,basename="album")



urlpatterns=[


]+router.urls