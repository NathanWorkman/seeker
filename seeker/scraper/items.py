# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem

from job.models import Job


class JobItem(DjangoItem):
    django_model = Job
    job_board = scrapy.Field()
    board_url = scrapy.Field()
    company = scrapy.Field()
    title = scrapy.Field()
    email = scrapy.Field()
    # url = scrapy.Field()
