from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.forms.formsets import formset_factory, BaseFormSet
from django.core.context_processors import csrf
from django.utils.translation import ugettext_lazy as _

from .models import Poll, Choice
from .forms import PollForm, ChoiceForm, ChoiceFormset

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


def vote(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    try:
        selected = poll.choice_set.get(pk=request.POST['choice'])
    except KeyError, Choice.DoesNotExist:
        return TemplateResponse(request, 'polls/details.html', {
            'poll': poll,
        })
    else:
        selected.votes += 1
        selected.save()
        return HttpResponseRedirect('/polls/' + poll_id + '/results')


def create(request):
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False

    Formset = formset_factory(
        ChoiceForm, max_num=10, formset=RequiredFormSet
    )

    if request.method == 'POST':
        main_form = PollForm(request.POST)
        formset = Formset(request.POST, request.FILES)
        if main_form.is_valid() and formset.is_valid():
            poll, created = Poll.objects.get_or_create(
                question=main_form.cleaned_data.get('question'),
                pub_date=main_form.cleaned_data.get('pub_date')
            )
            for choice in formset.forms:
                choice = choice.save(commit=False)
                choice.poll = poll
                choice.save()
            return HttpResponseRedirect('/polls')

    args = {}
    args.update(csrf(request))
    args['form'] = PollForm()
    args['formset'] = Formset()
    args['class'] = 'add'
    args['title'] = _('Add New Poll')
    args['btn'] = _('Add Poll')

    return TemplateResponse(request, 'polls/form.html', args)


def update(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    if request.method == 'POST':
        formset = ChoiceFormset(request.POST, request.FILES, instance=poll)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/polls')

    args = {}
    args.update(csrf(request))
    args['form'] = PollForm(instance=poll)
    args['formset'] = ChoiceFormset(instance=poll)
    args['class'] = 'update'
    args['title'] = _('Update Poll')
    args['btn'] = _('Update Poll')

    return TemplateResponse(request, 'polls/form.html', args)


