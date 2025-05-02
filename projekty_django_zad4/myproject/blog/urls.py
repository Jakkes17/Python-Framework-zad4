from django.urls import path
from .views import post_list

urlpatterns = [
    path('posts/', post_list, name='post_list'),
]
from django.urls import path
from .views import PostListAPIView

urlpatterns = [
    path('posts/', post_list, name='post_list'),  # jeśli masz ten widok z zadania 2
    path('api/posts/', PostListAPIView.as_view(), name='api_post_list'),
]
