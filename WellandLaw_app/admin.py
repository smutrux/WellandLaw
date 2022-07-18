from django.contrib import admin
from . models import BoardMember, ExternalLink, Event, MemberForm, EventForm, ContactForm, Job

admin.site.register(BoardMember)
admin.site.register(ExternalLink)
admin.site.register(Event)
admin.site.register(MemberForm)
admin.site.register(EventForm)
admin.site.register(ContactForm)
admin.site.register(Job)
