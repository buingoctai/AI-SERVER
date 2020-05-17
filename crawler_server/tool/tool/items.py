import scrapy


class Article(scrapy.Item):
    # define the fields for your item here like:

    domain = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    topic = scrapy.Field()
    crawlDate = scrapy.Field()
    imageUrl = scrapy.Field()
