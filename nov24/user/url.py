from django.urls import path
from . import views
from knox.views import LogoutView
urlpatterns = [
    path('register/', views.CreateUserAPI.as_view()),
    path('update-user/<int:pk>/', views.UpdateUserAPI.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('advertiser-profile/', views.CreateAdvertiserProfileAPIView.as_view()),
    path('influencer-profile/', views.CreateInfluencerProfileAPIView.as_view()),
    path('influencer-profile/<int:pk>/', views.InfluencerProfileAPIView.as_view()),
    path('advertiser-profile/<int:pk>/', views.AdvertiserProfileAPIView.as_view()),
]
