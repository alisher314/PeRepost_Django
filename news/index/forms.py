from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, News

# Готовая форма с изменениями
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control bg-dark text-white', 'rows': 3, 'placeholder': 'Оставьте комментарий...'})
        }

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['news_title', 'news_des', 'news_photo', 'news_category']  # Поля из модели