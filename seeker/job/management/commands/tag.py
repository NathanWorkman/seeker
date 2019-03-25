import requests
import time

from django.core.management.base import BaseCommand
from seeker.job.models import Job, Tag


class Command(BaseCommand):
    help = "This function removes all 'N/A' strings and sets to empty value"

    def _tag_jobs(self):
        jobs = Job.objects.all()
        for job in jobs:
            try:
                if "Python" in job.body:
                    print(job.id)
            except Exception as e:
                print('Something went wrong!')
                print(e)
                pass

    def handle(self, *args, **options):
        self._tag_jobs()
