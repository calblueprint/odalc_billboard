from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

from odalc_billboard.app.models import Submission


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['content', 'points', 'submitted']
    readonly_fields = ['content', 'points', 'submitted']


admin.site.register(Submission, SubmissionAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)
