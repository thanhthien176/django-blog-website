from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("allposts/", views.AllPostsView.as_view(), name="all-posts"),
    path("categories/<slug:slug>", views.CategoryView.as_view(), name="category"),
    path("<slug:slug>", views.DetailPostView.as_view(), name="detail-post"),
    path("add/", views.CreatePostView.as_view(), name="add-post"),
    path("<slug:slug>/edit", views.EditPostView.as_view(), name="edit-post"),
    path("<slug:slug>/delete", views.DeletePostView.as_view(), name="delete-post"),
    path("about/", views.AboutView, name="about"),
    path("search/", views.SearchPostView, name="search_posts"),
]
