from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem


class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["cafebiz.com"]
    start_urls = [
        "https://cafebiz.vn/wefit-bat-ngo-tuyen-bo-pha-san-chu-tiem-spa-than-troi-cong-no-len-toi-gan-200-trieu-em-cung-phai-dong-cua-spa-theo-thoi-20200511171050497.chn",
    ]

    def parse(self, response):
        question = Selector(response).xpath(
            '//div[@class="content"]/div[@class="w640right"]/div[@class="detail-content"]/p')

        for question in question:
            item = CrawlerItem()

            item['User'] = question.xpath(
                'text()').extract_first()
            item['Comment'] = question.xpath(
                'text()').extract_first()
            item['Time'] = question.xpath(
                'text()').extract_first()

            yield item

        # item = CrawlerItem()
        # item['User'] = question.xpath(
        #     'h1/text()').extract_first()
        # item['Time'] = "khong co"

        # subquestion = Selector(question).xpath(
        #     '//div[@class="w640right"]/div[@class="detail-content"]/p')
        # print("subquestion=", subquestion)
        # for sub in subquestion:
        #     item['Comment'] = item['Comment']+sub.xpath(
        #         'text()').extract_first()

        # yield item
