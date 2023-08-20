from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView

app_name = BlogsConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('create', BlogCreateView.as_view(), name='blog_create'),
    path('update/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
]
