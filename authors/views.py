from django.shortcuts import render
from django.views.generic import CreateView
from .models import Author

# Create your views here.
class CreateAuthorView(CreateView):
    model = Author
    template_name = "authors/form-author.html"
    