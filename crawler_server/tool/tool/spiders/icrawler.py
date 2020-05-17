from scrapy import Spider, Request
from scrapy.selector import Selector
from tool.items import Article
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import HtmlResponse


class IcrawlerSpider(Spider):
    name = 'icrawler'

    allowed_domains = ["tuoitre.vn"]
    start_urls = [
        'https://congnghe.tuoitre.vn/'
    ]

    def parse(self, response):
        if response.url == 'https://congnghe.tuoitre.vn/':
            lastedArticlesList = response.css(
                'ul.list-news-content li a::attr(href)').getall()
            print('########## lastedArticlesList=', lastedArticlesList)
            lastedArticlesList = list(dict.fromkeys(lastedArticlesList))
            print('##################### lastedArticlesList=', lastedArticlesList)
            for link in lastedArticlesList:
                print("################## link=", link)

                request = Request('https://tuoitre.vn/'+link,
                                  callback=self.parse)
                yield request
        else:
            # print('########## response.url=', response.url)
            title = response.css('h1.article-title::text').get()
            imageUrl = response.css(
                'div.main-content-body img::attr(src)').get()
            if imageUrl is None:
                imageUrl = "data:image/jpeg;base64,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"

            content = ''
            intro = response.xpath(
                '//*[@id="mainContentDetail"]/div/div[2]/h2/text()').get()
            content = content+intro
            contentList = Selector(response).xpath(
                '//*[@id="main-detail-body"]/p')
            for subContent in contentList:
                sub = subContent.xpath('text()').get()
                if sub is None:
                    continue
                else:
                    content = content+sub
            article = Article()
            article['domain'] = self.allowed_domains[0]
            article['title'] = title
            article['content'] = content
            article['topic'] = self.start_urls[0]
            article['imageUrl'] = imageUrl
            yield article
