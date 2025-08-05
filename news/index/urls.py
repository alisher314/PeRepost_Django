from django.urls import path
from . import views

app_name = 'index' # Рекомендуется: определить app_name для пространств имен

urlpatterns = [
    path('', views.home_page),
    path('views.category/<int:pk>', views.category_page, name='category_page'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('register/', views.register, name='register')
]