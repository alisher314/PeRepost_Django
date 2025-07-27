from django.urls import path
from . import views

app_name = 'index' # Рекомендуется: определить app_name для пространств имен

urlpatterns = [
    path('', views.home_page)
]