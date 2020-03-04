from scrapy.spiders import XMLFeedSpider
from scraper.items import JobItem

from django.utils import timezone


class DjangoGigsSpider(XMLFeedSpider):
    name = 'djangogigs'
    allowed_domains = ['djangogigs.com']
    start_urls = ['https://djangogigs.com/feeds/gigs/']
    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        item = JobItem()
        item['title'] = node.xpath('title/text()').extract_first()
        # item['title'] = str('test')
        item['company'] = str('Django Gigs')
        item['body'] = node.xpath('description/text()').extract()
        item['pub_date'] = node.xpath('pubDate/text()').extract_first()
        item['url'] = node.xpath('link/text()').extract_first()
        item['scrape_date'] = timezone.now()
        item['job_board'] = "Django Gigs"
        item['board_url'] = "www.djangogigs.com"
        item['email'] = ''
        item['salary'] = ''
        item['location'] = ''
        item["company_url"] = ''
        return item
