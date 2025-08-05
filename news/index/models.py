from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewsCategory(models.Model):
    news_category_name = models.CharField(max_length=32)
    added_date = models.DateTimeField(auto_now_add=True)

    # Рекомендуется добавить метод __str__ для лучшего отображения в админке
    def __str__(self):
        return self.news_category_name

    class Meta:
        verbose_name_plural = 'Categories'


class News(models.Model):
    news_title = models.CharField(max_length=128)  # Исправлено: max_length
    news_des = models.TextField()
    news_photo = models.ImageField(upload_to='media') # Исправлено: ImageField
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    # Рекомендуется добавить метод __str__ для лучшего отображения в админке
    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name_plural = 'News'


class Banner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banners/')
    url = models.URLField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_date']

    def __str__(self):
        return self.title


class Ad(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ads/')
    url = models.URLField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Реклама"


class Comment(models.Model):
    news = models.ForeignKey('News', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField("Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий от {self.author} к {self.news}"