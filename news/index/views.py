from django.shortcuts import render
from .models import NewsCategory, News

# Create your views here.
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