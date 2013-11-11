from django.conf.urls import patterns, include, url


urlpatterns = patterns('blog.views',
    url(r'^$', 'index', name='blog-home'),
    url(r'^post/(?P<slug>[^\.]+)', 'posts',  name='blog-post'),
    url(r'^category/(?P<slug>[^\.]+)', 'categories', name='blog-category'),
    url(r'^category.form$', 'category_form', name='blog-category-form'),
)
