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
        instances = 20
        for x in range(instances):
            submission = Submission(
                content=self.sd.sentence(),
                points=self.sd.int(min_value=-20, max_value=20),
                submitted=self.sd.past_datetime(0, 10000)
            )
            submission.save()
        print 'Generating submissions...'
