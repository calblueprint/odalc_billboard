from django import forms

from odalc_billboard.app.models import Submission

class SubmissionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SubmissionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Submission
        fields = ['content']
