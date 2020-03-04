import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scraper.items import JobItem
from scrapy.http import Request

from seeker.job.models import SearchTerms

from django.utils import timezone


class GreenHouseSpider(Spider):
    name = "greenhouse"
    allowed_domains = ["google.com"]

    def search_query(self):
        search_terms = list(SearchTerms.objects.all())
        query_items = []
        for term in search_terms:
            query_items.append(str(term))

        query = "q=site:greenhouse.io+{}&tbs=qdr:m".format("+".join(query_items))
        return query

    def start_requests(self):
        search_query = self.search_query()
        base_url = "https://www.google.com/search?"
        start_urls = []

        start_urls.append(base_url + search_query)

        return [scrapy.http.Request(url=start_url) for start_url in start_urls]

    def parse(self, response):
        """Extract job detail urls from response."""
        hxs = Selector(response)
        urls = hxs.xpath('//div[contains(@class, "r")]/a/@href').extract()
        for url in urls:
            url = url.replace("/url?q=", "")
            yield Request(url, callback=self.parse_detail_pages, dont_filter=True)
            print(url)

    def parse_detail_pages(self, response):
        hxs = Selector(response)
        jobs = hxs.xpath('//div[contains(@id, "app_body")]')
        items = []
        for job in jobs:
            item = JobItem()
            item["title"] = job.xpath('//h1[contains(@class, "app-title")]/text()').extract_first()
            item["company"] = job.xpath('//span[contains(@class, "company-name")]/text()').extract_first()
            item["body"] = job.xpath('//div[contains(@id, "content")]').extract()
            item["location"] = job.xpath('//div[contains(@class, "location")]').extract_first()
            item["url"] = response.request.url
            item["pub_date"] = str('n/a')
            item["email"] = str('n/a')
            item["salary"] = str('n/a')
            item["scrape_date"] = timezone.now()
            item["job_board"] = "Greenhouse"
            item["board_url"] = "www.greenhouse.io"
            item["company_url"] = ''
            items.append(item)
        return items
