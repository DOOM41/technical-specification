from django.urls import path
from apps.menu import views


urlpatterns = [
    path('<str:menu_name>', views.MenuView.as_view(), name='menu')
]
