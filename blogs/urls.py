from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("categories/<slug:slug>", views.CategoryView.as_view(), name="category"),
    path("<slug:slug>", views.DetailPostView.as_view(), name="detail-post")
]
