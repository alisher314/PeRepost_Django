# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import NewsCategory, News, Banner, Ad
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views import View
from .forms import RegisterForm



# Главная страница
def home_page(request):
    news = News.objects.all().order_by('-added_date')
    categories = NewsCategory.objects.all()

    # Получаем все активные баннеры из базы данных
    active_banners = Banner.objects.filter(is_active=True).order_by('added_date')

    # --- Вот здесь мы добавляем логику для получения рекламного баннера ---
    try:
        ad = Ad.objects.filter(is_active=True).first()
    except Ad.DoesNotExist:
        ad = None
    # ----------------------------------------------------------------------

    context = {
        'news': news,
        'categories': categories,
        'banners': active_banners,
        'ad': ad,  # Добавляем наш баннер в контекст
    }

    return render(request, 'home.html', context)


# Теперь вы можете удалить функцию my_view, так как она больше не нужна,
# либо убедиться, что она нигде не используется.

# Остальные функции остаются без изменений
def category_page(request, pk):
    category = get_object_or_404(NewsCategory, id=pk)
    news_list = News.objects.filter(news_category=category)
    return render(request, 'category.html', {
        'category': category,
        'news_list': news_list
    })


def news_detail(request, news_id):
    # Получаем объект новости по ID или возвращаем ошибку 404
    news = get_object_or_404(News, pk=news_id)

    # --- Создаём словарь 'context' и передаём в него данные ---
    context = {
        'news': news,
    }
    # --------------------------------------------------------

    # Теперь 'context' определён и может быть передан в шаблон
    return render(request, 'news_detail.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('index:home')  # Замени на свой URL главной страницы
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def custom_logout(request):
    logout(request)  # очищаем сессию пользователя
    return redirect('/')  # редиректим на главную страницу

