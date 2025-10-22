from django import forms
from django.forms import inlineformset_factory
from .models import Post, Section, Tag

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'author','summary', 'tag','image']
        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':"Enter the post's title",
                'style':"font-size: 16px",
            }),
            'author': forms.Select(attrs={
                "class":"form-select",
                "style": "font-size: 16px; width: 80%;",
            }),
            'summary': forms.Textarea(attrs={
                "class":"form-control",
                "placeholder":"Enter content of the post",
                "style":"font-size: 16px",
            }),
                  
            }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        self.fields['author'].empty_label = "Select author"

# SectionForm
class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['title','image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the section's title!",
                "style": "font-size: 16px"
            }),
            'content': forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter the section's content...",
                "style": "font-size: 16px"
            })
        }

# SectionFormset
SectionFormSet = inlineformset_factory(
    Post,
    Section,
    form= SectionForm,
    fields=['title', 'content','image','order'],
    extra=1,
    can_delete=True,
)
