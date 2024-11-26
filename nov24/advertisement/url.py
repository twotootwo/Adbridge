from django.urls import path
from . import views

urlpatterns = [
    path('create-advertisement/', views.CreateAdvertisementAPIView.as_view()),
    path('get-all-advertisement/', views.AllAdvertisementAPIView.as_view()),
    path('get-advertisement/<str:account>/', views.AdvertisementAPIView.as_view()),
    path('update-advertisement/<str:account>/', views.AdvertisementAPIView.as_view()),
    path('delete-advertisement/<str:account>/', views.AdvertisementAPIView.as_view()),
]
