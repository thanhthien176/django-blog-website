from django.urls import path
from . import views

urlpatterns = [
    path("add-author/", views.CreateAuthorView.as_view(), name="add-author")
]
