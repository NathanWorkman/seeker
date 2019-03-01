from suit.menu import ParentItem
from suit.apps import DjangoSuitConfig
from django.apps import AppConfig


class JobConfig(DjangoSuitConfig):
    layout = 'horizontal'
    menu = (
        ParentItem('Jobs', url='/job/job/'),
        ParentItem('Companies', url='/company/company/'),
        ParentItem('Job Boards', url='/job/board/'),
        ParentItem('Cron Logs', url='/django_cron/cronjoblog/'),
        ParentItem('Search Terms', url='/job/searchterms/'),
    )

    def ready(self):
        # import jobs.signals  # noqa
        super(JobConfig, self).ready()
