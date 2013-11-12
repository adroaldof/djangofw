from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.response import TemplateResponse
from django.utils.translation import ugettext_lazy as _

from .forms import BlogForm, CategoryForm
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


def post_form(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog')

    args = {}
    args.update(csrf(request))
    args['form'] = BlogForm()
    args['class'] = 'add'
    args['title'] = _('Add New Post')
    args['btn'] = _('Add Post')

    return TemplateResponse(request, 'blog/form.html', args)


def post_delete(request, post_id):
    post = get_object_or_404(Blog, id=post_id)

    if post:
        post.delete()
        return HttpResponseRedirect('/blog')


def categories(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Blog.objects.filter(category=category)[:5]
    return TemplateResponse(request, 'blog/categories.html', {
        'category': category,
        'posts': posts,
    })


def category_form(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog')

    args = {}
    args.update(csrf(request))
    args['form'] = CategoryForm()
    args['class'] = 'add'
    args['title'] = _('Add New Category')
    args['btn'] = _('Add Category')

    return TemplateResponse(request, 'blog/form.html', args)


def category_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if category:
        category.delete()
        return HttpResponseRedirect('/blog')
