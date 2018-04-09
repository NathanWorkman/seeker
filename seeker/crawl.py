from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

setting = get_project_settings()
process = CrawlerProcess(setting)
# https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.CrawlerProcess

for spider in process.spiders.list():
    print("Running spider %s" % (spider))
    process.crawl(spider)

process.start()
