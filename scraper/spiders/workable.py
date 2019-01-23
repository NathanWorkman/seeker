import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scraper.items import JobItem
from scrapy.http import Request

from django.utils import timezone


class WorkableSpider(Spider):
    name = "workable"
    allowed_domains = ["google.com"]

    def start_requests(self):
        search_query = "q=site:workable.com+django&tbs=qdr:m"
        base_url = "https://www.google.com/search?"
        start_urls = []

        start_urls.append(base_url + search_query)

        return [scrapy.http.Request(url=start_url) for start_url in start_urls]

    def parse(self, response):
        """Extract job detail urls from response."""
        hxs = Selector(response)
        urls = hxs.xpath('//cite/text()').extract()
        for url in urls:
            yield Request(url, callback=self.parse_detail_pages, dont_filter=True)
            print(url)

    def parse_detail_pages(self, response):
        hxs = Selector(response)
        jobs = hxs.xpath('//main[contains(@class, "stacked")]')
        items = []
        for job in jobs:
            item = JobItem()
            item["title"] = job.xpath('//h1/text()').extract_first()
            item["company"] = str('n/a')
            item["body"] = job.xpath('//main[contains(@class, "stacked")]').extract()
            item["location"] = job.xpath('//p[contains(@class, "meta")]').extract_first()
            item["url"] = response.request.url
            item["pub_date"] = str('n/a')
            item["email"] = str('n/a')
            item["salary"] = str('n/a')
            # item["tags"] = job.css('.-tags p a.post-tag::text').extract()
            item["scrape_date"] = timezone.now()
            item["job_board"] = "Workable"
            item["board_url"] = "www.workable.com"
            items.append(item)
        return items