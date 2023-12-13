from django import forms
from .models import Post, Job
from django_quill.forms import QuillFormField

class PostForm(forms.ModelForm):
    content = QuillFormField()
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
