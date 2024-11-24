from django.urls import path
from . import views

urlpatterns = [
    path('create-advertisement/', views.AdvertisementAPIView.as_view()),
    path('get-advertisement/', views.AdvertisementAPIView.as_view()),
    path('update-advertisement/<int:pk>/', views.AdvertisementAPIView.as_view()),
    path('delete-advertisement/<int:pk>/', views.AdvertisementAPIView.as_view()),
]
