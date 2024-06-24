from django.urls import path

from api.views import AlbumViewsetView,Track_mixin,signUp_view,Review_addView,review_Mixin

from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import ObtainAuthToken


router=DefaultRouter()

router.register("album",AlbumViewsetView,basename="album")
router.register("reg",signUp_view,basename="reg")



urlpatterns=[

    path('track/<int:pk>/',Track_mixin.as_view(),name="track"),
    path("token/",ObtainAuthToken.as_view(),name="token"),
    path("review_add/<int:pk>/",Review_addView.as_view(),name="review_add"),
    path("review/<int:pk>/",review_Mixin.as_view(),name="review"),



]+router.urls