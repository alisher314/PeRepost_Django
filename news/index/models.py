from django.db import models

# Create your models here.
class NewsCategory(models.Model):
    news_category_name = models.CharField(max_length=32)
    added_date = models.DateTimeField(auto_now_add=True)

    # Рекомендуется добавить метод __str__ для лучшего отображения в админке
    def __str__(self):
        return self.news_category_name


class News(models.Model):
    news_title = models.CharField(max_length=128)  # Исправлено: max_length
    news_des = models.TextField()
    news_photo = models.ImageField(upload_to='media') # Исправлено: ImageField
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    # Рекомендуется добавить метод __str__ для лучшего отображения в админке
    def __str__(self):
        return self.news_title