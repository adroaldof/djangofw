from django.contrib import admin
from polls.models import Poll, Choice


class ChoiceInline(admin.TabularInline):
    '''
    Create an inline choice field with 3 forms that will be placed
    on poll creation
    '''
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    '''
    How display a form to new poll and polls informarion
    '''
    # Split form in fieldsets
    fieldsets = [
        ('Question Information', {'fields': ['question']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
    # Place above inline form
    inlines = [ChoiceInline,]
    # Poll display list
    list_display = ('question', 'pub_date', 'was_published_recently',)
    # Add list filter
    list_filter = ['pub_date',]
    # Add search fields
    search_fields = ['question',]
    # Add date hierachy
    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)