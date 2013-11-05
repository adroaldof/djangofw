from django.conf.urls import patterns, url


urlpatterns = patterns('polls.views',
    # localhost:8000/polls
    url(r'^$', 'home', name='polls-home'),
    # localhost:8000/polls/5
    url(r'^(?P<poll_id>\d+)$', 'detail', name='polls-detail'),
)
