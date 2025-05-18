from django.urls import path
from . import views

app_name = 'menu'  # Добавляем пространство имен

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Явно указываем name='login'
    path('menu/', views.menu_list, name='menu'),
    path('checkout/', views.checkout, name='checkout'),
    path('', views.login_redirect, name='root'),  # Редирект с главной
]