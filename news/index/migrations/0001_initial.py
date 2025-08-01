# Generated by Django 5.2.4 on 2025-07-27 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_category_name', models.CharField(max_length=32)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=128)),
                ('news_des', models.TextField()),
                ('news_photo', models.ImageField(upload_to='media')),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('news_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.newscategory')),
            ],
        ),
    ]
