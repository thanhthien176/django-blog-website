from django.db import models
from django.utils.text import slugify

from authors.models import Author




# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = slugify(self.tag)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.tag
    
    
class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="post", blank=True, null=True)
    summary = models.CharField(max_length=300, null=True, blank=True)
    tag = models.ManyToManyField(Tag, related_name="posts", null=True, blank=True)
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    slug = models.SlugField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            count = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"


class Section(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="sections")
    title = models.CharField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to="section")
    
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.title}"
    