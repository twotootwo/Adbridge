# logg/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from logg import views


urlpatterns = [
    #path('', views.login_view, name='login'),  # /login/ 경로에 CustomLoginView 연결
    path('', views.LoginView.as_view(), name='login'),  # /login/ 경로에 CustomLoginView 연결
    #path('next/', views.hello, name='hello'),
    path('sign-up/',views.SignupView.as_view(),name="sign_up"),
    #path('inf/',views.InfluenceView.as_view(),name="inf"),
    path('inf/',views.ad_list_view,name="inf"),
    path('adv/',views.AdvertiseView.as_view(),name="adv"),
    path('postform/',views.PostingView.as_view(),name="post_form"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
