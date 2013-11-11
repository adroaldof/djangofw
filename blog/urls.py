from django.conf.urls import patterns, include, url


urlpatterns = patterns('blog.views',
    url(r'^$', 'index', name='blog-home'),
    url(r'^post/(?P<slug>[^\.]+)', 'posts',  name='blog-post'),
    url(r'^post.form$', 'post_form',  name='blog-post-form'),
    url(r'^post.delete/(?P<post_id>\d+)', 'post_delete',  name='blog-post-delete'),
    url(r'^category/(?P<slug>[^\.]+)', 'categories', name='blog-category'),
    url(r'^category.form$', 'category_form', name='blog-category-form'),
    url(r'^category.delete/(?P<category_id>\d+)', 'category_delete', name='blog-category-delete'),
)
