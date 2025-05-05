from django.urls import path
from . import views
from . import user_views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('category/new/', views.CategoryCreateView.as_view(), name='category_create'),  # Movida antes del patrón con slug
    path('category/<slug:slug>/', views.CategoryPostListView.as_view(), name='category_detail'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
    path('register/', user_views.register, name='register'),
]