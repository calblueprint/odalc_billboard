from django.core.management.base import BaseCommand

from odalc_billboard.app.models import Submission

from sampledatahelper.helper import SampleDataHelper
from sampledatahelper.model_helper import ModelDataHelper


class Command(BaseCommand):
    args = ''
    help = 'Generate seed data for submissions'
    sd = SampleDataHelper()
    md = ModelDataHelper()

    def handle(self, *args, **options):
        print 'Generating submissions...'
        self.md.fill_model(Submission, 20)
