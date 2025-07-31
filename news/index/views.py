from itertools import product

from django.shortcuts import render
from .models import NewsCategory, News

# Create your views here.
#Главная страница
def home_page(request):
    # Получаем все новости из базы данных
    news = News.objects.all()
    # Получаем все категории новостей из базы данных
    categories = NewsCategory.objects.all()

    # Создаем словарь контекста, который будет передан в шаблон
    cntext = {
        'news': news,          # Переменная 'news' в шаблоне будет содержать все объекты News
        'categories': categories # Переменная 'categories' в шаблоне будет содержать все объекты NewsCategory
    }

    # Возвращаем отрендеренный шаблон 'home.html', передавая в него созданный контекст
    return render(request, 'home.html', cntext) # <-- ИСПРАВЛЕНО: добавлен аргумент 'cntext'

# Страница с новостями по категории
def category_page(request, pk):
    category = Category.objects.get(id=pk)
    news = News.objects.filter(news_category=category)
    cntext = {
        'category': category,
        'news': news
    }
    return render(request, 'category.html, cntext')

# Страница с определенными новостями
def news_page(request, pk):
    news = News.objects.get(id=pk)
    cntext = {
        'news': news
    }
    return render(request, 'news.html', cntext)
