# Create your views here.
from django.template.response import TemplateResponse
from .models import Blog, Category


def index(request):
    categories = Category.objects.all()
    posts = Blog.objects.all()[:5]
    return TemplateResponse(request, 'blog/index.html', {
        'categories': categories,
        'posts': posts,
    })


