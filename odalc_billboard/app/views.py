import json

from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView, View

from odalc_billboard.app.models import Submission
from odalc_billboard.app.forms import SubmissionForm

SORT_HOT = 'hot'
SORT_NEW = 'new'
SORT_TOP = 'top'

class IndexView(TemplateView):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        submission_form = context['submission_form']
        if '_submission' in request.POST:
            if submission_form.is_valid():
                submission_form.save()
                return redirect(request.path)
                print "Bad submission"
            else:
                return self.render_to_response(self.get_context_data())
                print "Bad submission"
        elif '_donate' in request.POST:
            #TODO: Stripe donations
            pass
        else:
            return redirect(request.path)

    def dispatch(self, request, *args, **kwargs):
        self.sort = request.GET.get('sort', SORT_HOT)
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        if self.sort == SORT_NEW:
            context['submissions'] = Submission.objects.all()
        elif self.sort == SORT_TOP:
            context['submissions'] = Submission.objects.all().order_by('-points')
        else:
            context['submissions'] = Submission.objects.sorted_hot()
        if self.request.method == 'POST':
            context['submission_form'] = SubmissionForm(self.request.POST)
        else:
            context['submission_form'] = SubmissionForm()
        return context


class AJAXVoteView(View):
    def get(self, request, *args, **kwargs):
        print "got a get request"
        content = json.dumps({})
        return HttpResponse(content, content_type='text/plain; charset=x-user-defined')

    def post(self, request, *args, **kwargs):
        print "got a post request"
        content = json.dumps({})
        return HttpResponse(content, content_type='text/plain; charset=x-user-defined')
