from django.conf.urls import patterns, url


urlpatterns = patterns('polls.views',
    url(r'^$', 'home', name='polls-home'),
)