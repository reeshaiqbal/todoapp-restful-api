from django.urls import path
from .views import SignupAPI
from .views import LoginAPI

urlpatterns = [
    path('signup/', SignupAPI.as_view()),
    path('login/', LoginAPI.as_view()),
]
