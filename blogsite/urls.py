from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blogpost-list/', views.BlogPostListView.as_view(), name='blogpost-list'),
    path('blogpost/<pk>', views.BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('bloggers', views.BloggerListView.as_view(), name="bloggers"),
    path('blogger/<pk>', views.BloggerDetailView.as_view(), name="blogger-detail"),
    path('blogpost/<pk>/add_comment/', views.add_comment, name="add-comment"),

]