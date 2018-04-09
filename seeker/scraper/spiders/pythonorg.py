from scrapy.spiders import XMLFeedSpider
from scraper.items import JobItem

from django.utils import timezone


class PythonOrgSpider(XMLFeedSpider):
    name = 'pythonorg'
    allowed_domains = ['python.org']
    start_urls = ['https://www.python.org/jobs/feed/rss/']
    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        item = JobItem()
        item['title'] = node.xpath('title/text()').extract_first()
        item['company'] = 'Python.org'
        item['body'] = node.xpath('description/text()').extract()
        item['pub_date'] = 'n/a'
        item['url'] = node.xpath('link/text()').extract_first()
        item["scrape_date"] = timezone.now()
        item["job_board"] = "Python.org"
        item["board_url"] = "www.python.org"
        item["email"] = 'n/a'
        item["salary"] = 'n/a'
        item['location'] = 'n/a'
        return item
