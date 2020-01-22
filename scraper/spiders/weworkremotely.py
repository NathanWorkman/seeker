# # import scrapy
# from scrapy.spiders import Spider
# from scrapy.selector import Selector
# from scraper.items import OrganizationItem
# from scrapy.http import Request

# from django.utils import timezone

# from seeker.job.models import ZipCodes

# search_terms = [
#     'hvac',
#     'pest control',
#     'window washer',
#     'electrician',
#     'plumber',
#     'carpet cleaning',
#     'appliance repair',
#     'commercial cleaning',
#     'eletrical contracting',
#     'landscaping',
#     'lawn care',
#     'painters',
#     'pool and spa services',
#     'pressure washing',
#     'roofing',
#     'snow removal',
#     'tree removal'
# ]
# locations = []
# generated_start_urls = []

# print(generated_start_urls)


# zip_codes = ZipCodes.objects.filter(yp_searched=False).order_by('id')[:50]
# for zip_code in zip_codes:
#     search_location = zip_code.zip_code
#     zip_id = zip_code.id
#     obj = ZipCodes.objects.get(id=zip_id)
#     obj.yp_searched = True
#     obj.save()
#     locations.append(search_location)


# for term in search_terms:
#     for location in locations:
#         url = "http://www.yellowpages.com/search?search_terms={}&geo_location_terms={}".format(term, location)
#         generated_start_urls.append(url)


# class YellowPagesSpider(Spider):
#     name = "yellowpages"
#     base_url = 'http://www.yellowpages.com'
#     start_urls = generated_start_urls

#     # print("*" * 200)
#     # print(start_urls)
#     # print("*" * 200)

#     def parse(self, response):
#         """Extract job detail urls from response."""
#         hxs = Selector(response)
#         urls = hxs.xpath('//a[contains(@class, "business-name")]/@href').extract()
#         for url in urls:
#             schema = '{}{}'.format('https://www.yellowpages.com', url)
#             yield Request(schema, callback=self.parse_detail_pages, dont_filter=True)
#             # print(url)

#         # pagination
#         next_link = hxs.xpath('//a[contains(text(),"Next")]/@href').extract()
#         if next_link:
#             next_link = next_link[0]
#             # print(next_link)
#             yield Request(self.base_url + next_link, self.parse, dont_filter=True)

#     def parse_detail_pages(self, response):
#         hxs = Selector(response)
#         item = OrganizationItem()
#         company = hxs.xpath('//div[@id="content-container"]')

#         name = company.xpath('.//div[contains(@class, "sales-info")]/h1/text()').extract()
#         if name:
#             name = name[0]
#             item['name'] = name
#         else:
#             item['name'] = ''

#         email = company.xpath('.//a[contains(@class,"email-business")]/@href').extract()
#         if email:
#             email = email[0]
#             item['email'] = email
#         else:
#             item['email'] = ''

#         full_address = company.xpath('.//h2[contains(@class, "address")]/text()').extract()
#         if full_address:
#             full_address = full_address[0]
#             item['full_address'] = full_address
#         else:
#             item['full_address'] = ''

#         # check = company.xpath('.//p[contains(@class, "address")]/span[4]/text()').extract()

#         # if check:
#         #     address = company.xpath('.//p[contains(@class, "address")]/span[1]/text()').extract()
#         #     if address:
#         #         address = address[0]
#         #         item['address'] = address
#         #     else:
#         #         item['address'] = ''

#         #     city = company.xpath('.//p[contains(@class, "address")]/span[2]/text()').extract()
#         #     if city:
#         #         city = city[0]
#         #         item['city'] = city
#         #     else:
#         #         item['city'] = ''

#         #     state = company.xpath('.//p[contains(@class, "address")]/span[3]/text()').extract()
#         #     if state:
#         #         state = state[0]
#         #         item['state'] = state
#         #     else:
#         #         item['state'] = ''

#         #     zip_code = company.xpath('.//p[contains(@class, "address")]/span[4]/text()').extract()
#         #     if zip_code:
#         #         zip_code = zip_code[0]
#         #         item['zip_code'] = zip_code
#         #     else:
#         #         item['zip_code'] = ''
#         # else:
#         #     item['address'] = ''

#         #     city = company.xpath('.//p[contains(@class, "address")]/span[1]/text()').extract()
#         #     if city:
#         #         city = city[0]
#         #         item['city'] = city
#         #     else:
#         #         item['city'] = ''

#         #     state = company.xpath('.//p[contains(@class, "address")]/span[2]/text()').extract()
#         #     if state:
#         #         state = state[0]
#         #         item['state'] = state
#         #     else:
#         #         item['state'] = ''

#         #     zip_code = company.xpath('.//p[contains(@class, "address")]/span[3]/text()').extract()
#         #     if zip_code:
#         #         zip_code = zip_code[0]
#         #         item['zip_code'] = zip_code
#         #     else:
#         #         item['zip_code'] = ''

#         phone = company.xpath('.//p[contains(@class, "phone")]/text()').extract()
#         if phone:
#             phone = phone[0]
#             item['phone'] = phone
#         else:
#             item['phone'] = ''

#         url = company.xpath('.//a[contains(text(),"Visit Website")]/@href').extract()
#         if url:
#             url = url[0]
#             item['url'] = url
#         else:
#             item['url'] = ''

#         description = company.xpath('.//dd[contains(@class, "general-info")]/text()').extract()
#         if description:
#             description = description[0]
#             item['description'] = description
#         else:
#             item['description'] = ''

#         organization_type = company.xpath('.//dd[contains(@class, "categories")]/span[1]/a/text()').extract()
#         if organization_type:
#             organization_type = organization_type[0]
#             item["organization_type"] = organization_type
#         else:
#             item["organization_type"] = ''

#         item["address"] = ''
#         item["city"] = ''
#         item["state"] = ''
#         item["zip_code"] = ''
#         item["rate"] = ''
#         item["lat"] = ''
#         item["lng"] = ''
#         item["lat_lng"] = ''
#         item["twitter"] = ''
#         item["facebook"] = ''
#         item["linkedin"] = ''
#         item["instagram"] = ''
#         item["source"] = 'Yellow Pages'
#         item["scrape_date"] = timezone.now()
#         # print(item)
#         yield item
