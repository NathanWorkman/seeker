import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scraper.items import JobItem
from django.utils import timezone


class StackOverflowSpider(Spider):
    name = "stackoverflow"
    allowed_domains = ["stackoverflow.com"]

    def __init__(self, search_params='django python', *args, **kwargs):
        super(StackOverflowSpider, self).__init__(*args, **kwargs)

        if not search_params:
            raise ValueError("No search terms given")

        self.search_terms = search_params.split(",")

    def start_requests(self):
        search_query = "q=django&r=true&sort=p"
        base_url = "https://stackoverflow.com/jobs?"
        start_urls = []

        start_urls.append(base_url + search_query)

        return [scrapy.http.Request(url=start_url) for start_url in start_urls]

    def parse(self, response):
        hxs = Selector(response)
        jobs = hxs.xpath('//div[contains(@class, "-job-item")]')
        items = []
        for job in jobs:
            item = JobItem()
            item["title"] = job.xpath('.//a[@class="job-link"]/text()').extract_first()
            item["company"] = job.xpath('.//div[@class="-name"]/text()').extract()
            item["body"] = job.xpath('.//div[@class="-name"]/text()').extract()
            item["location"] = job.xpath('.//div[@class="-location"]/text()').extract()[0].strip()
            item["url"] = job.xpath('.//a[@class="job-link"]/@href').extract()[0]
            item["pub_date"] = job.xpath('.//p[contains(@class, "-posted-date")]/text()').extract()[0].strip()
            item["email"] = "N/A"
            item["salary"] = job.xpath('.//span[@class="-salary"]/text()').extract_first(default='n/a').strip()
            # item["tags"] = job.css('.-tags p a.post-tag::text').extract()
            item["scrape_date"] = timezone.now()
            item["job_board"] = "Stack Overflow"
            item["board_url"] = "www.stackoverflow.com"
            items.append(item)
        return items
