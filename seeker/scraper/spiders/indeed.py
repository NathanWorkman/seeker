import scrapy

from scrapy.spiders import Spider
from scrapy.selector import Selector

from scraper.items import JobItem

from django.utils import timezone


class IndeedSpider(Spider):
    name = "indeed"
    allowed_domains = ["indeed.com"]
    # start_urls = ["https://www.indeed.com/q-Django-l-remote-jobs.html"]
    start_urls = [
        "https://www.indeed.com/jobs?q=django&l=Remote&limit=50",
    ]
    handle_httpstatus_list = [301, 302]

    # def start_requests(self):
    #     # location = ""
    #     # distance = ""
    #     # search_terms = "django"
    #     # search_query = "q="
    #     base_url = "https://www.indeed.com/jobs?q=Django&l=remote"
    #     start_urls = []
    #     start_urls.append(base_url)

    #     return [scrapy.http.Request(url=start_url) for start_url in start_urls]

    def parse(self, response):
        # self.log('\n Crawling  %s\n' % response.url)
        hxs = Selector(response)
        jobs = hxs.xpath('//td[@id="resultsCol"]/div')
        items = []
        for job in jobs:
            item = JobItem()

            item['title'] = job.xpath('h2/a/@title/text()').extract()
            item['url'] = job.xpath('h2/a').extract()
            item['location'] = str('n/a')

            # item['location'] = job.xpath('span[@class="location"]/span/text()').extract()

            # Not all entries have a company
            if job.xpath("span[@class='company']/text()").extract() == []:item['company'] = [u'']
            else:
                item['company'] = job.xpath("span[@class='company']/text()").extract()
            item["email"] = str('n/a')
            item['body'] = job.xpath(
                "table/tr/td/span[@class='summary']").extract()
            item['salary'] = job.xpath(
                "table/tr/td/span[@class='source']/text()").extract()
            item['pub_date'] = job.xpath(
                "table/tr/td/span[@class='date']/text()").extract()
            item["scrape_date"] = timezone.now()
            item["job_board"] = "Indeed"
            item["board_url"] = "www.indeed.com"
            items.append(item)
        return items
