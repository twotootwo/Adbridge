from django.urls import path

import users
from users.views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/<int:pk>/', ProfileView.as_view())
]
