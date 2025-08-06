# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import NewsCategory, News, Banner, Ad
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views import View
from .forms import RegisterForm, CommentForm, NewsForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

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
    categories = NewsCategory.objects.all()  # ✅ Добавлено
    return render(request, 'category.html', {
        'category': category,
        'news_list': news_list,
        'categories': categories
    })


def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    categories = NewsCategory.objects.all()  # ✅ Добавлено
    comments = news.comments.all().order_by('-created_at')

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.news = news
                comment.author = request.user
                comment.save()
                return redirect('index:news_detail', news_id=news.id)
        else:
            return redirect('login')  # Перенаправляем на логин, если не авторизован
    else:
        form = CommentForm()

    context = {
        'news': news,
        'categories': categories,
        'comments': comments,
        'form': form,
    }
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


# Проверка: только админ
def is_admin(user):
    return user.is_superuser  # Можно заменить на user.is_staff, если нужно

@method_decorator(user_passes_test(is_admin), name='dispatch')
class NewsCreateView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'add_news.html'
    success_url = reverse_lazy('index:home')  # После добавления новости возвращаемся на главную