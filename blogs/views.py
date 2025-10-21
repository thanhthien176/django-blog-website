from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse, reverse_lazy

from .models import Post

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "blogs/index.html"
    
    
    def get_queryset(self):
        return Post.objects.order_by("-created_at")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_queryset()
        context["featured_post"] = post.first()
        context["posts"] = post[:3]
        return context