"""
URL configuration for Youtube project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('adyoutubepage/', views.index_video_data,name='index_video_data'),
    path('detailpage/', views.channel_data,name='channel_video_statistics'),
    path('adinstagrampage/',views.instagram_data,name='instagram_post_details'),
]#여기에 youtube/video_statistics까지 써놓기

