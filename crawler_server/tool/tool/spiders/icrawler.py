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

class CrawlerSpider(Spider):
    name = 'icrawler'
  
    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]

    def parse(self, response):
        print("--------in parse-----, response=",response)
        
        
        # doc=CrawlerItem()
        # doc['url'] = response.url
        # yield doc
        item = CrawlerItem()
        # questions = Selector(response).xpath('//div[@class="detail-content"]/p/text()').getall()
        # questions=  Selector(response).css('p::text').getall()
        questions=Selector(response).css('h1.title::text').extract()
        item['content']=questions

        # for question in questions:
        #     item = CrawlerItem()
        #     item['content'] = question.xpath(
        #         'text()').extract_first()
        
    
        yield item