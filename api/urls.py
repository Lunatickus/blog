from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserViewSet.as_view({'get': 'list'})),
    path('users/<int:pk>/', views.UserViewSet.as_view({'get': 'retrieve'})),

    path('posts/', views.PostViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/<int:pk>/', views.PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('comments/', views.CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('comments/<int:pk>/', views.CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('categories/', views.CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('categories/<int:pk>/', views.CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)