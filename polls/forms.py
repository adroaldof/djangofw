from django import forms
from django.forms.models import inlineformset_factory

from .models import Poll, Choice


class PollForm(forms.ModelForm):
    #pub_date = forms.DateField(widget=forms.DateTimeField())
    class Meta:
        model = Poll


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = ['poll', 'votes',]
