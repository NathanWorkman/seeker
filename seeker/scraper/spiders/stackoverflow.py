from scrapy.spiders import XMLFeedSpider
from scraper.items import JobItem

from django.utils import timezone


class StackOverflowSpider(XMLFeedSpider):
    name = 'stackoverflow'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['https://stackoverflow.com/jobs/feed?q=django&r=true']
    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        item = JobItem()
        item['title'] = node.xpath('title/text()').extract_first().split('(', 1)[0]
        item['company'] = node.xpath('name/text()').extract()
        item['body'] = node.xpath('description/text()').extract()
        item['pub_date'] = node.xpath('pubDate/text()').extract_first()
        item['url'] = node.xpath('link/text()').extract_first()
        item["scrape_date"] = timezone.now()
        item["job_board"] = "Stack Overflow"
        item["board_url"] = "www.stackoverflow.com"
        item["email"] = str('n/a')
        item["salary"] = str('n/a')
        if node.xpath('location/text()'):
            item['location'] = node.xpath('location/text()').extract_first()
        else:
            item['location'] = str('n/a')
        return item
