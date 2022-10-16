from django.urls import path
from . import views

urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("shorten",views.ShortenURL,name="shorten"),
    path("go/<str:sht_url>",views.GoPageRedirect,name="gopage"),
]
