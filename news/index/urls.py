from django.urls import path
from . import views

app_name = 'index' # Рекомендуется: определить app_name для пространств имен

urlpatterns = [
    path('', views.home_page),
    path('views.category/<int:pk>', views.category_page),
    path('news/<int:pk>', views.news_page)
]