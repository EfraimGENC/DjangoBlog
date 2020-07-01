"""
article app URL Configuration
"""
from django.contrib import admin
from django.urls import path
from article import views

app_name = 'article'

urlpatterns = [
    path('dashboard/', views.dashboard,name='dashboard'),
    path('addarticle/', views.addArticle,name='addarticle'),
    path('article/<int:id>', views.detail,name='detail'),
    path('author/<str:author>', views.authorsArticles, name='authorsArticles'),
    path('update/<int:id>', views.articleUpdate, name='articleUpdate'),
    path('delete/<int:id>', views.articleDelete, name='articleDelete'),
    path('', views.allArticles, name='allArticles'),
    path('comments/<int:id>', views.addComments, name='comments'),
]