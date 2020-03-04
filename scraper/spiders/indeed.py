from scrapy.spiders import XMLFeedSpider
from scraper.items import JobItem

from django.utils import timezone


class IndeedSpider(XMLFeedSpider):
    name = 'indeed'
    allowed_domains = ['indeed.com']
    start_urls = ['http://rss.indeed.com/rss?q=django&l=remote']
    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        item = JobItem()
        item['title'] = node.xpath('title/text()').extract_first()
        item['company'] = node.xpath('source/text()').extract_first()
        item['body'] = node.xpath('description/text()').extract()
        item['pub_date'] = node.xpath('pubDate/text()').extract_first()
        item['url'] = node.xpath('link/text()').extract_first()
        item["scrape_date"] = timezone.now()
        item["job_board"] = "Indeed"
        item["board_url"] = "www.indeed.com"
        item["email"] = str('n/a')
        item["salary"] = str('n/a')
        item['location'] = str('n/a')
        item["company_url"] = ''
        return item
