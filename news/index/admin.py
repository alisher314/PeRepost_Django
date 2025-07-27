from django.contrib import admin
from .models import News, NewsCategory

# Register your models here.
admin.site.register(NewsCategory)
admin.site.register(News)
