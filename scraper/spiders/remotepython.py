from scrapy.spiders import XMLFeedSpider
from scraper.items import JobItem

from django.utils import timezone


class RemotePythonSpider(XMLFeedSpider):
    name = 'remotepython'
    allowed_domains = ['remotepython.com']
    start_urls = ['https://www.remotepython.com/latest/jobs/feed/']
    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        item = JobItem()
        item['title'] = node.xpath('title/text()').extract_first()
        item['company'] = 'Remote Python'
        item['body'] = node.xpath('description/text()').extract()
        item['pub_date'] = 'n/a'
        item['url'] = node.xpath('link/text()').extract_first()
        item["scrape_date"] = timezone.now()
        item["job_board"] = "Remote Python"
        item["board_url"] = "www.remotepython.com"
        item["email"] = 'n/a'
        item["salary"] = 'n/a'
        item['location'] = 'n/a'
        item["company_url"] = ''
        return item
