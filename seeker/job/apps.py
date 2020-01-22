from django.apps import AppConfig


class JobConfig(AppConfig):

    def ready(self):
        # import jobs.signals  # noqa
        super(JobConfig, self).ready()
