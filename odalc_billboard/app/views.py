from django.db.models import F
from django.http import HttpResponse, Http404
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
        print request.POST
        if request.POST.get('content-validator') != u'':
            # if content-validator is not empty, then it's a bot
            raise Http404("You done goofed.")
        if '_submission' in request.POST:
            if submission_form.is_valid():
                submission = submission_form.save()
                request.session[str(submission.id)] = 1
                return redirect('/?sort=new')
            else:
                return self.render_to_response(self.get_context_data())
        else:
            return redirect(request.path)

    def dispatch(self, request, *args, **kwargs):
        self.sort = request.GET.get('sort', SORT_TOP)
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['is_hot'] = self.sort == SORT_HOT
        context['is_top'] = self.sort == SORT_TOP
        context['is_new'] = self.sort == SORT_NEW
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
    def post(self, request, *args, **kwargs):
        submission_id = request.POST.get('postId')
        diff = int(request.POST.get('diff'))
        is_up = request.POST.get('isUpClicked') == 'true'
        is_down = request.POST.get('isDownClicked') == 'true'
        submission = Submission.objects.get(id=submission_id)
        submission.points = F('points') + diff
        submission.save()
        if is_up:
            request.session[str(submission.id)] = 1
        elif is_down:
            request.session[str(submission.id)] = -1
        else:
            request.session.pop(str(submission.id), None)
        request.session.modified = True
        return HttpResponse('')
