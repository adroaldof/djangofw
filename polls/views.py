from django.template.response import TemplateResponse


def home(request):
    latests_poll_list = Poll.objects.order_by('-pub_date')[:15]
    return TemplateResponse(request, 'polls/index.html', {
        'latests_poll_list': latests_poll_list,
    })


