from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse, reverse_lazy

from .models import Post
from .forms import PostForm, SectionFormSet

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
    
class AllPostsView(ListView):
    model = Post
    template_name = "blogs/list-posts.html"
    context_object_name = "posts"
    
class CategoryView(ListView):
    model = Post
    template_name = "blogs/list-posts.html"
    context_object_name = "posts"
    
class DetailPostView(DetailView):
    model = Post
    template_name = "blogs/detail-post.html"
    context_object_name = "post"
    
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blogs/form-post.html"
    success_url = reverse_lazy("add-post")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.POST:
            context['formset'] = SectionFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = SectionFormSet()
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            # sections = formset.save(commit=False)
            # for section in sections:
            #     section.post = self.object
            #     section.save()
            
            return redirect(self.get_success_url())

        else:
            return self.form_invalid(form)
    

class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blogs/form-post.html"
    
    def get_success_url(self):
        return reverse("detail-post", kwargs={'slug':self.object.slug})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = SectionFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = SectionFormSet(instance=self.object)
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            sections = formset.save(commit=False)
            for section in sections:
                section.post = self.object
                section.save()
            formset.save_existing_objects()
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)
    

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blogs/delete-post.html'
    context_object_name = "post"
    
    def get_success_url(self):
        return reverse_lazy("all-posts")
    
def AboutView(request):
    return render(request, "blogs/about.html")