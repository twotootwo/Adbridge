from django.urls import path, include

from advertiserList import views

urlpatterns = [
    path('', views.advertiser_list, name="advertiser's list"),
]