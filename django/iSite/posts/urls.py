from django.urls import path
from . import views
from .views import PostListView, postCreate, postUpdate, PostDetailView, PostDeleteView, UserPostsView


urlpatterns = [
    path('', PostListView.as_view(), name='posts-home'),
    path('post/new/', postCreate, name='posts-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='posts-detail'),
    path('post/<str:username>/', UserPostsView.as_view(), name='posts-user'),
    path('post/<int:pk>/update/', postUpdate, name='posts-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='posts-delete'),
    path('about/', views.about, name='posts-about'),
]