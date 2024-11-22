# logg/urls.py

from django.urls import path

from logg import views

urlpatterns = [
    path('', views.login_view, name='login'),  # /login/ 경로에 CustomLoginView 연결
    path('next/', views.hello, name='hello'),
    path('sign-up/',views.sign_up,name="sign_up"),

]
