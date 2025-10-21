from django.contrib import admin
from .models import Post, Section

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    
class SectionAdmin(admin.ModelAdmin):
    list_display = ("post", "title")
    
admin.site.register(Post, PostAdmin)
admin.site.register(Section, SectionAdmin)