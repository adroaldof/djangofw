from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from .models import Poll, Choice

def home(request):
    latests_poll_list = Poll.objects.order_by('-pub_date')[:15]
    return TemplateResponse(request, 'polls/index.html', {
        'latests_poll_list': latests_poll_list,
    })


def detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return TemplateResponse(request, 'polls/details.html', {
        'poll': poll,
    })


def results(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    choices = Choice.objects.filter(poll=poll)
    return TemplateResponse(request, 'polls/results.html', {
        'poll': poll,
        'choices': choices,
        'poll_id': poll_id,
    })


