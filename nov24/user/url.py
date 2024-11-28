from django.urls import path
from . import views
from knox.views import LogoutView
urlpatterns = [
    path('register/', views.CreateUserAPI.as_view()),
    #path('update-user/<str:account>/', views.UpdateUserAPI.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('advertiser-profile/', views.AdvertiserProfileAPIView.as_view()), # 전체 조회
    path('advertiser-profile/<str:account>/', views.CreateAdvertiserProfileAPIView.as_view()), # 생성, 조회, 수정
    path('influencer-profile/', views.InfluencerProfileAPIView.as_view()), # 전체 조회
    path('influencer-profile/<str:account>/', views.CreateInfluencerProfileAPIView.as_view()), # 생성, 조회, 수정

]
