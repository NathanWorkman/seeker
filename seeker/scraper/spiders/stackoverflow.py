import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scraper.items import JobItem
from scrapy.http import Request

from django.utils import timezone


class StackOverflowSpider(Spider):
    name = "stackoverflow"
    allowed_domains = ["stackoverflow.com"]

    def start_requests(self):
        search_query = "q=django&r=true&sort=p"
        base_url = "https://stackoverflow.com/jobs?"
        start_urls = []

        start_urls.append(base_url + search_query)

        return [scrapy.http.Request(url=start_url) for start_url in start_urls]

    def parse(self, response):
        """Extract job detail urls from response."""
        hxs = Selector(response)
        urls = hxs.xpath('//a[@class="job-link"]/@href').extract()
        for url in urls:
            yield Request('https://www.stackoverflow.com/' + url, callback=self.parse_detail_pages, dont_filter=True)

    def parse_detail_pages(self, response):
        hxs = Selector(response)
        jobs = hxs.xpath('//div[contains(@class, "-job-item")]')
        items = []
        for job in jobs:
            item = JobItem()
            item["title"] = job.xpath('//a[@class="title job-link"]/text()').extract_first()
            item["company"] = job.xpath('//div[@class="-company g-row"]/div[@class="-name"]/a/text()').extract()
            item["body"] = job.xpath('//section[@class="-job-description"]/node()').extract()
            item["location"] = "\n".join(job.xpath('//div[@class="-company g-row"]/div[@class="-location"]/text()').extract())
            item["url"] = response.request.url
            item["pub_date"] = str('n/a')
            item["email"] = str('n/a')
            item["salary"] = job.xpath('//div[@class="-description"]/div[@class="-perks g-row"]/p[@class="-salary"]/text()').extract_first(default='n/a').strip()
            # item["tags"] = job.css('.-tags p a.post-tag::text').extract()
            item["scrape_date"] = timezone.now()
            item["job_board"] = "Stack Overflow"
            item["board_url"] = "www.stackoverflow.com"
            items.append(item)
        return items
