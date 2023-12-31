from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path('login', views.login),
    re_path('singup', views.singup),
    re_path('test_token', views.test_token),
]
