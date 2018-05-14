import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scraper.items import JobItem
from scrapy.http import Request

from django.utils import timezone


class RecruiterBoxSpider(Spider):
    name = "recruiterbox"
    allowed_domains = ["google.com"]

    def start_requests(self):
        search_query = "q=site:recruiterbox.com+django&tbs=qdr:m"
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
        jobs = hxs.xpath('//div[contains(@id, "content")]')
        items = []
        for job in jobs:
            item = JobItem()
            item["title"] = job.xpath('//h1[contains(@class, "jobtitle")]/text()').extract_first()
            item["company"] = str('n/a')
            item["body"] = job.xpath('//div[contains(@class, "jobdesciption")]').extract()
            item["location"] = job.xpath('//span[contains(@class, "meta-job-location-city")]').extract()
            item["url"] = response.request.url
            item["pub_date"] = str('n/a')
            item["email"] = str('n/a')
            item["salary"] = str('n/a')
            item["scrape_date"] = timezone.now()
            item["job_board"] = "Recruiter Box"
            item["board_url"] = "www.recruiterbox.com"
            items.append(item)
        return items
