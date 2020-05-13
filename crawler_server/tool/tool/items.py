import scrapy

class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    
    content = scrapy.Field()