# views.py

from django.shortcuts import render, get_object_or_404
from .models import NewsCategory, News, Banner, Ad  # Убедитесь, что Ad импортирован


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
    # ...
    return render(request, 'category.html', context)


def news_detail(request, news_id):
    # ...
    return render(request, 'news_detail.html', context)