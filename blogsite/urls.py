from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blogpost-list/', views.BlogPostListView.as_view(), name='blogpost-list'),
    path('blogpost/<pk>', views.BlogPostDetailView.as_view(), name='blogpost-detail'),
]