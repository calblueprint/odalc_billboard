from datetime import datetime
import random

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
        instances = 50
        for x in range(instances):
            submission = Submission.objects.create(
                content=self.sd.sentence(),
                points=self.sd.int(min_value=-20, max_value=20),
            )
            submission.submitted = datetime(random.choice(range(2000, 2013)), random.choice(range(1,12)), random.choice(range(1,28)))
            submission.save()
        print 'Generating submissions...'
