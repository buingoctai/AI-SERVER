from scrapy import Spider
from scrapy.selector import Selector
from tool.items import CrawlerItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import HtmlResponse



class IcrawlerSpider(Spider):
    name = 'icrawler'

    allowed_domains = ["thegioididong.com"]
    start_urls = [
        "https://www.thegioididong.com/dtdd/samsung-galaxy-a50",
    ]

    def parse(self, response):
        questions = response.xpath('/html/body/section/div[7]/aside[1]/div[2]/article/h2/text()').get()
        item = CrawlerItem()
        item['text']=questions

        yield item

           