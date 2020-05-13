from scrapy import Spider
from scrapy.selector import Selector
from tool.items import CrawlerItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import HtmlResponse

# class IcrawlerSpider(CrawlSpider):
#     name = 'icrawler'

#     def __init__(self, *args, **kwargs):
#         # We are going to pass these args from our django view.
#         # To make everything dynamic, we need to override them inside __init__ method
#         self.url = kwargs.get('url')
#         self.domain = kwargs.get('domain')
#         self.start_urls = [self.url]
#         self.allowed_domains = [self.domain]

#         IcrawlerSpider.rules = [
#            Rule(self.extrac_data, callback='parse_item'),
#         ]
#         super(IcrawlerSpider, self).__init__(*args, **kwargs)

#     def extrac_data(self):
#         body = '<html><body><span>good</span></body></html>'
#         response = HtmlResponse(url='http://example.com', body=body)
#         Selector(response=response).xpath('//span/text()').get()
#     def parse_item(self, response):
#         # You can tweak each crawled page here
#         # Don't forget to return an object.
#         i = {}
#         i['url'] = response.url
#         return i


# class CrawlerSpider(Spider):
#     name = 'icrawler'

#     def __init__(self, *args, **kwargs):
#         self.url = kwargs.get('url')
#         # self.domain = kwargs.get('domain')
#         self.domain = ["blog.arrow-tech.vn"]
#         self.start_urls = [self.url]
#         self.allowed_domains = [self.domain]

#     def parse(self, response):
#         print("--------in parse-----, response=", response)

#         # doc=CrawlerItem()
#         # doc['url'] = response.url
#         # yield doc

#         #questions = Selector(response).xpath('//div[@class="content fck"]')
#         # questions=  Selector(response).css('p::text').getall()

#         item = CrawlerItem()
#         item['content'] = response.xpath(
#             '//div[@class="post-inner js-post-content"]/p/text()').extract()[0].strip()
#         print("-------in parse,------item=", item)
#         yield item


# class CrawlerSpider(Spider):
#     name = "icrawler"
#     allowed_domains = ["thegioididong.com"]
#     start_urls = [
#         "https://www.thegioididong.com/dtdd/samsung-galaxy-a50",
#     ]

#     def parse(self, response):
#         questions = Selector(response).xpath('//ul[@class="listcomment"]/li')

#         for question in questions:
#             item = CrawlerItem()

#             item['content'] = question.xpath(
#                 'div[@class="rowuser"]/a/strong/text()').extract_first()
#             item['content'] = question.xpath(
#                 'div[@class="question"]/text()').extract_first()
#             item['content'] = question.xpath(
#                 'div[@class="actionuser"]/a[@class="time"]/text()').extract_first()

#             yield item


class IcrawlerSpider(CrawlSpider):
    name = 'icrawler'

    def __init__(self, *args, **kwargs):
        # We are going to pass these args from our django view.
        # To make everything dynamic, we need to override them inside __init__ method
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]

        # IcrawlerSpider.rules = [
        #     Rule(LinkExtractor(unique=True), callback='parse_item'),
        # ]

        # super(IcrawlerSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        # You can tweak each crawled page here
        # Don't forget to return an object.
        divs = response.xpath(
            '//div[@class="content w980"]/div[@id="main-detail"]/div[@class="w980"]')
        for h1 in divs.xpath('.//h1'):
            result = h1.getall()
            item = CrawlerItem()
            item['content'] = result
            yield item
