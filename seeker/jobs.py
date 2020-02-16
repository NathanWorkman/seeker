import subprocess
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import (
    DjangoJobStore,
    register_events,
    register_job
)

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')


@register_job(scheduler, "interval", hours=1)
def run_spiders():
    # Runs all Spiders
    subprocess.run(["python seeker/crawl.py"], shell=True)


@register_job(scheduler, "interval", hours=1)
def fetch_new_proxies():
    # curl -sSf "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt" > proxy-list.txt
    subprocess.run(["curl -sSf https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt > ./data/proxy-list.txt"], shell=True)  # noqa
    # print("Fetched new proxies")


@register_job(scheduler, "interval", hours=2)
def fetch_new_proxies_secondary():
    # curl -sSf "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt" > proxy-list.txt
    subprocess.run(["curl -sSf https://www.proxy-list.download/api/v1/get?type=http&anon=elite&country=US > ./data/proxy-list.txt"], shell=True)  # noqa
    # print("Fetched secondary proxies")


register_events(scheduler)
scheduler.start()
