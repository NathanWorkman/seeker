import subprocess

# import scrapy
# from scrapy.utils.project import get_project_settings
# from scrapy import spiderloader
# from scrapy.utils import project

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import (
    DjangoJobStore,
    register_events,
    register_job
)

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')


@register_job(scheduler, "interval", minutes=60)
def run_spiders():
    spiders = [
        'djangogigs',
        'greenhouse',
        'indeed',
        'lever',
        'pythonorg',
        'recruiterbox',
        'remotepython',
        'stackoverflow',
        'workable'
    ]
    # settings = project.get_project_settings()
    # spider_loader = spiderloader.SpiderLoader.from_settings(settings)
    # spiders = spider_loader.list()

    for spider in spiders:
        print(spider)
        subprocess.run(["scrapy", "crawl", spider])
    # print(spiders)
    # subprocess.run(["scrapy", "crawl", "greenhouse"])

register_events(scheduler)
scheduler.start()
