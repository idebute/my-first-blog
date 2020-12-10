from django.urls import path
from . import views  # все views (представления) из приложения blog

# URL-шаблон
urlpatterns = [
    path('', views.post_list, name='post_list'),
]