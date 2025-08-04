from django.contrib import admin
from .models import News, NewsCategory, Banner, Ad

# Register your models here.
admin.site.register(NewsCategory)
admin.site.register(News)

# Регистрация новой модели Banner
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'added_date')
    list_filter = ('is_active',)
    search_fields = ('title',)

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title',)