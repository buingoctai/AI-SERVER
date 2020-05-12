import scrapy

class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    
    User = scrapy.Field()
    Comment = scrapy.Field()
    Time = scrapy.Field()