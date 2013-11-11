# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template.response import TemplateResponse
from .models import Blog, Category


def index(request):
    categories = Category.objects.all()
    posts = Blog.objects.all()[:5]
    return TemplateResponse(request, 'blog/index.html', {
        'categories': categories,
        'posts': posts,
    })


def posts(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    return TemplateResponse(request, 'blog/posts.html', {
        'post': post,
    })


def categories(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Blog.objects.filter(category=category)[:5]
    return TemplateResponse(request, 'blog/categories.html', {
        'category': category,
        'posts': posts,
    })


