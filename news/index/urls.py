from django.urls import path
from . import views
from .views import NewsCreateView

app_name = 'index' # Рекомендуется: определить app_name для пространств имен

urlpatterns = [
    path('', views.home_page, name='home'),
    path('views.category/<int:pk>', views.category_page, name='category_page'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('add-news/', NewsCreateView.as_view(), name='add_news'),
    path('register/', views.register, name='register')
]