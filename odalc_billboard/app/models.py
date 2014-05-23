from datetime import datetime, timedelta
import operator

from django.db import models


EPOCH = datetime(1970, 1, 1)

def epoch_seconds(date):
    """Returns the number of seconds from the epoch to date."""
    td = date - EPOCH
    return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)


class SubmissionManager(models.Manager):
    def sorted_hot(self, *args, **kwargs):
        qs = self.raw('SELECT * FROM app_submission a ORDER BY hot(a.points, a.submitted) DESC;')
        return qs


class Submission(models.Model):
    content = models.TextField(
        'Submission Content',
        max_length=100,
    )
    points = models.IntegerField(
        'Submission Points',
        default=1,
    )
    submitted = models.DateTimeField(
        'Submitted Datetime',
        auto_now_add=True
    )

    objects = SubmissionManager()

    def __unicode__(self):
        return 'ID %d @ %s | %d POINTS' % (self.id, self.submitted, self.points)

    class Meta:
        ordering = ['-submitted']
