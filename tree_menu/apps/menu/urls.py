from django.urls import path
from apps.menu import views


urlpatterns = [
    path('', views.MenuView.as_view(), name='menu')
]
