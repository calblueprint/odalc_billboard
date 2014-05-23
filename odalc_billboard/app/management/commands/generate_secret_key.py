from django.utils.crypto import get_random_string

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    args = ''
    help = 'Generate a new secet key'

    def handle(self, *args, **options):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        get_random_string(50, chars)
        print "Secret Key:"
        print get_random_string(50, chars)
