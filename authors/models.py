from django.db import models
from django.utils.text import slugify



# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    born_date = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to="authors", null=True, blank=True)
    summary = models.TextField()
    slug = models.SlugField(blank=True)
    
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.full_name())
            slug = base_slug
            count = 1
            while Author.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            
            self.slug = slug
            
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.fullname()